import re
import os
from nltk.tokenize import sent_tokenize


dir_name = os.path.dirname(__file__)
file_names = ["Georgi Stamatov Vestovoj Dimo",
              "Girltalk",
              "Ivan Vazov Chichovtzi",
              "Ladislav Klima Novel",
              "Robert Sheckley Skulking Permit",
              "Bulgarian parliament Meetings",
              "Bulgarian parliament Recorded Sessions – part 1",
              "Bulgarian parliament Recorded Sessions – part 2",
              "Bulgarian parliament Recorded Sessions – part 3",
              "Bulgarian parliament Recorded Sessions – part 4",
              "Bulgarian parliament Recorded Sessions – part 5",
              "Bulgarian parliament Recorded Sessions – part 7",
              "Bulgarian President News – part 1",
              "Bulgarian President News – part 2",
              "Bulgarian President News – part 3",
              "Bulgarian President News – part 4",
              "Bulgarian President News – part 5"]

for file_name in file_names:
    full_file_name = os.path.join(dir_name, "../{0}/{1}.txt")

    file = open(full_file_name.format("raw", file_name), "r")
    text = file.read()

    text_with_reduced_new_lines = re.sub('(\\n)+', '\\n', text)
    text_with_new_lines_after_ellipsis = re.sub('… ([А-Я])', '…\\n\\1', text_with_reduced_new_lines)

    if file_name in ["Bulgarian President News – part 1", "Bulgarian President News – part 2",
                     "Bulgarian President News – part 3", "Bulgarian President News – part 4",
                     "Bulgarian President News – part 5"]:
        text_without_timing_and_stars = re.sub('(\[.*\||\* \* \*)', '', text_with_new_lines_after_ellipsis)
        tokenized_text = sent_tokenize(text_without_timing_and_stars)
    else:
        tokenized_text = sent_tokenize(text_with_new_lines_after_ellipsis)

    with open(full_file_name.format("processed", file_name), "w") as fout:
        for sentence in tokenized_text:    
            print(sentence, file=fout)

    file = open(full_file_name.format("processed", file_name), "r")
    text = file.read()

    text_only_sent_beginning_on_new_line = re.sub('\\n([а-я]|– [а-я]|[^А-Я–"0-9A-Za-z-‘(])', '\\1', text)
    text_with_sentences_on_one_line = re.sub('(\.|“)( |(„))*([А-Я])', '\\1\\n\\3\\4', text_only_sent_beginning_on_new_line)

    with open(full_file_name.format("processed", file_name), "w") as fout:
        print(text_with_sentences_on_one_line, file=fout)

# Manual clean up:
# Delete references in the end of some of the files.
# Delete some portions.
# Add some missing punctuation.
# Remove chapter numbering.
# Fix some new lines that shouldn't have been caused by проф., р., гр., ending of a line not on a punctuation.
# Remove non-sentences - '^.*[а-я]\\n' -> ''
# Remove dates - '^[0-9].*г.\\n' -> ''
# Remove points in lists - '^[0-9].\\n' -> ''
# Turn titles into sentences where possible.
# Split sentences on separate lines where the previous sentence ends on a quotation mark. - '([.?!…])"([А-Я])', '([.?!…])" ([А-Я])'
# Add missing spaces - '!–' -> '! –'; '\?–' -> '? –'; '\?…' -> '? …'; '\.–' -> '. –'; '!…' -> '! …'
# Delete lines like these: – – –
# Investigate where short dashes are used - [^(?<=по|най)]- - and switch to long dashes at some of the places / delete some dashes

