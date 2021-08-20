import re
import os
from nltk.tokenize import sent_tokenize


dir_name = os.path.dirname(__file__)

file = open(os.path.join(dir_name, "../raw/Bibliia.txt"), "r")
text = file.read()

text_with_reduced_tabs = re.sub('(\\t)+', '\\t', text)
text_with_reduced_new_lines = re.sub('(\\n)+', '\\n', text_with_reduced_tabs)
text_with_references_on_one_line = re.sub('\\n\\t((гл\.)|(ст\.))', '', text_with_reduced_new_lines)
text_without_references = re.sub('\\t\([0-9]+\).*?\\n', '', text_with_references_on_one_line)
text_without_numbered_words = re.sub('(?<=([а-яА-Я]|[.!?,;"*]))[0-9]+','',text_without_references)
text_without_references_words = re.sub('(?<=[а-яА-Я])(\*)+','',text_without_numbered_words)
text_without_explained_words = re.sub('\\t(\*)+.*?\\n', '', text_without_references_words)
text_without_numbered_lines = re.sub('\\t[0-9]+\s', '', text_without_explained_words)
text_without_new_lines_and_tabulations = re.sub('(\\n)+', ' ', text_without_numbered_lines)
text_without_tabulations = re.sub('(\\t)+', ' ', text_without_new_lines_and_tabulations)
tokenized_text = sent_tokenize(text_without_tabulations)
tokenized_text_cut_beginning = tokenized_text[23:]

with open(os.path.join(dir_name, "../processed/Bibliia_clean.txt"), "w") as fout:
    for sentence in tokenized_text_cut_beginning:    
        print(sentence, file=fout)

## Some manual cleaning up - where there were formatting discrepancies (mainly with references) and dashes interpreted wrongly as dialogue.



