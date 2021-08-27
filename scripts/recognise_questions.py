import classla
import sys


def recognise_question(sentence):
    nlp = classla.Pipeline('bg', processors='tokenize,pos')
    doc = nlp(sentence)
    processed_sentence = doc.to_dict()[0][0]

    starts_with_interrogative_word = processed_sentence[0]['xpos'].startswith('Pi') or len(processed_sentence) > 1 and processed_sentence[0]['xpos'] == 'R' and processed_sentence[1]['xpos'].startswith('Pi')
    contains_interrogative_particle = any([word['xpos'] == 'Ti' for word in processed_sentence])
    ends_on_interrogative_particle_a = processed_sentence[-1]['xpos'] != 'punct' and processed_sentence[-1]['text'] == 'а' or processed_sentence[-1]['xpos'] == 'punct' and processed_sentence[-2]['text'] == 'а'

    return starts_with_interrogative_word or contains_interrogative_particle or ends_on_interrogative_particle_a


if __name__ == '__main__':
    print(recognise_question(sys.argv[1]))
        


