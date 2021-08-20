import re
import os


dir_name = os.path.dirname(__file__)
full_file_name = os.path.join(dir_name, "../processed/Bibliia_clean.txt")

file = open(full_file_name, "r")
text = file.read()

text_with_sentences_on_one_line = re.sub('\. ([А-Я])', '.\\n\\1', text)
text_without_titles_only_sentences = re.sub('.*[А-Яа-я]\\n', '', text)

with open(full_file_name, "w") as fout:
    print(text_with_sentences_on_one_line, file=fout)

