import os
import re
from nltk.tokenize import sent_tokenize
from operator import itemgetter


dir_name = os.path.dirname(__file__)
directories = ['C-Culture', 'D-Society', 'E-Economy',
               'J-Politics', 'S-Military', 'Z']

for directory in directories:
    full_dir_name = os.path.join(dir_name, "../data/BNC/raw/JOURNALISM.BG/C-MassMedia", directory)

    for file_name in os.listdir(full_dir_name):
        file = open(os.path.join(full_dir_name, file_name), "r")
        text = file.read()

        text_only_sentences = ' '.join(map(itemgetter(0), re.findall('([А-Я].*(\.|\?|\!))', text)))
        tokenized_text = sent_tokenize(text_only_sentences)

        with open("{0}/{1}.txt".format(re.sub('/raw/', '/processed/', full_dir_name), os.path.split(full_dir_name)[1]), "a") as fout:
            for sentence in tokenized_text:    
                print(sentence, file=fout)

### Post-processing steps:
#1) Go through lines with '.', '?' and '!' in the middle followed by a capital letter and split the line if it consists of two separate sentences: '([.?!]) ([А-Я])' -> '\1\n\2'
#2) Clean up title meta-information about city and country at the beginning of some of the lines: '^[А-Я ]*,.*?-- ' (and similar regular expressions) -> ''
#3) Search for and fix misguided sentence splitting caused by the shortening of some words: '(млн\.|млрд\.|т\.е\.|т\.нар\.|вкл\.|т\.ч\.|др\.|т\.н\.|гр\.|Св\.|св\.|пр\.|сл\.|Хр\.|г\.|ул\.|н\.е\.|кв\.|дол\.|проф\.|ген\.|полк\.)\n' -> '\1 '
#4) Check for short words appearing at the end of the sentence in case there are shortened words not part of the list in #4: ' (["А-Яа-я.]{1,5})\n([^А-Я])' -> ' \1 \2'
### Also check for small words when they are followed by a capital letter -> Something like: ' (["А-Яа-я.]{1,3})\n([А-Я])' -> ' \1 \2'   
#5) Remove/replace such HTML codes - &lt;b&gt; &lt;/b&gt; &lt;I&gt; &lt;/I&gt; &amp;
#6) Split lines containing ellipsises in the middle being followed by a non-capital letter: '… ([^а-я])' -> '…\n\1'
#7) Find lines that don't start with a capital letter and merge with the previous line if the sentence was falsely split up: '\n([^А-Я])' -> ' \1'
#8) Find lines that don't end on a sentence break punctuation symbol and merge with next sentence if neded: '[^.?!]\n'
#9) Use standand quotation symbols  everywhere - " - and replace "--" with "-" in cases it is meant like "-"
#10) Replace "–" with "-" due to inconsistencies in using dashes.
