import re
import os


dir_name = os.path.dirname(__file__)
full_file_name = os.path.join(dir_name, "../processed/Bibliia_clean.txt")

file = open(full_file_name, "r")
text = file.read()

text_with_sentences_on_one_line = re.sub('\. ([А-Я])', '.\\n\\1', text)
text_with_sentences_ending_on_quotation_mark_on_one_line = re.sub('([.?!])"[0-9]* ([А-Я])', '\\1"\\n\\2', text_with_sentences_on_one_line)
text_without_titles_only_sentences = re.sub('.*[А-Яа-я]\\n', '', text_with_sentences_ending_on_quotation_mark_on_one_line)
text_without_references_following_quotation_mark = re.sub('"[0-9]', '"', text_without_titles_only_sentences)
text_without_references_following_closing_bracket = re.sub('\)[0-9]', ')', text_without_titles_only_sentences)


with open(full_file_name, "w") as fout:
    print(text_without_titles_only_sentences, file=fout)

### Manual clean-up:
#1) Investigate if end of sentence signs in the middle of the sentence - [.?!][^\n]+?
#2) Investigate lines starting with a small letter word - ^[а-я] - and fix if necessary
#3) Replace "–" with a regular dash "-" due to ASCII reasons

