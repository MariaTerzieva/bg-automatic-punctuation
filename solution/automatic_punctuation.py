import inquirer
from modules.data_prep import data_prep
from modules.classify import *
from difflib import SequenceMatcher
from wasabi import color
from signal import signal, SIGINT


MAIN_MENU = [
    inquirer.List('action',
                  message="Какво искате да направите?",
                  choices=["Автоматична пунктуация на текст", "Изход"])
]

INPUT_QUESTION = [
  inquirer.List('input',
                message="Откъде да взема входните данни?",
                choices=["Аз ще въведа текст.", "От файл."])
]

USER_INPUT_PROMPT = [
  inquirer.Text('text',
                message="Моля, въведете Вашия текст")
]

FILE_INPUT_PROMPT = [
  inquirer.Path('input_file_path',
                message='Моля, дайте пълния път до файла',
                path_type=inquirer.Path.FILE,
                exists=True,
                normalize_to_absolute_path=True)
]

OUTPUT_QUESTION = [
  inquirer.List('output',
                message="Къде да насоча изходните данни?",
                choices=["Към потребителския изход (екрана).", "Към файл."])
]

FILE_OUTPUT_PROMPT = [
  inquirer.Path('output_file_path',
                message='Моля, дайте пълния път до мястото, където да се запази файлът',
                path_type=inquirer.Path.FILE,
                normalize_to_absolute_path=True)
]

def handler(signal_received, frame):
    print("Прекратена операция.")
    exit()


def diff_strings(original_string, edited_string):
    output = []

    matcher = SequenceMatcher(None, original_string, edited_string)
    for opcode, original_string_1, original_string_2, edited_string_1, edited_string_2 in matcher.get_opcodes():
      if opcode == "equal":
        output.append(original_string[original_string_1:original_string_2])
      elif opcode == "insert":
        output.append(color(edited_string[edited_string_1:edited_string_2], fg=16, bg="green"))
      elif opcode == "delete":
        output.append(color(original_string[original_string_1:original_string_2], fg=16, bg="red"))
      elif opcode == "replace":
        output.append(color(edited_string[edited_string_1:edited_string_2], fg=16, bg="green"))
        output.append(color(original_string[original_string_1:original_string_2], fg=16, bg="red"))

    return "".join(output)


if __name__ == '__main__':
  signal(SIGINT, handler)

  main_menu_answers = inquirer.prompt(MAIN_MENU)

  while main_menu_answers['action'] != "Изход":
    answers = inquirer.prompt(INPUT_QUESTION)

    if answers['input'] == "Аз ще въведа текст.":
      user_input = inquirer.prompt(USER_INPUT_PROMPT)
      contents = [user_input['text']]
    else:
      file_input = inquirer.prompt(FILE_INPUT_PROMPT)

      with open(file_input['input_file_path'], "r") as f:
        print("Прочитане на входния файл...")
        print("Натиснете CTRL + C, за да прекратите операцията и да излезете от системата.")
        contents = f.read().splitlines()

    answers = inquirer.prompt(OUTPUT_QUESTION)

    if answers['output'] == "Към файл.":
      file_output = inquirer.prompt(FILE_OUTPUT_PROMPT)
    else:
      file_output = None

    print("Поставяне на пунктуация в текста...")
    print("Натиснете CTRL + C, за да прекратите операцията и да излезете от системата.")

    model_features, original_sentences = data_prep(contents)
    predicted_punctuation = predict_punctuation(model_features)
    punctuated_sentences = punctuate(original_sentences, predicted_punctuation)

    if file_output:
      with open(file_output['output_file_path'], "w") as f:
        print("Записване на резултатите в изхдния файл...")
        print("Натиснете CTRL + C, за да прекратите операцията и да излезете от системата.")

        for sentence in punctuated_sentences:
          print(sentence, file=f)   
    else:
      print("Вашият текст с автоматично поставена пунктуация:")
      for original_sentence, punctuated_sentence in zip(contents, punctuated_sentences):
        print(diff_strings(original_sentence, punctuated_sentence))

    main_menu_answers = inquirer.prompt(MAIN_MENU)

  exit()
  