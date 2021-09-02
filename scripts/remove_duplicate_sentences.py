import sys
import re


sentences_seen = set()
duplicate_sentences_file_name = 'data/Duplicate Sentences.txt'
input_file_names = ['data/Bible/processed/Bibliia_clean.txt',
                    'data/BulTreeBank/processed/Atanas Dalchev Fragments.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Meetings.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 1.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 2.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 3.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 4.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 5.txt',
                    'data/BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 7.txt',
                    'data/BulTreeBank/processed/Bulgarian President News – part 1.txt',
                    'data/BulTreeBank/processed/Bulgarian President News – part 2.txt',
                    'data/BulTreeBank/processed/Bulgarian President News – part 3.txt',
                    'data/BulTreeBank/processed/Bulgarian President News – part 4.txt',
                    'data/BulTreeBank/processed/Bulgarian President News – part 5.txt',
                    'data/BulTreeBank/processed/Georgi Stamatov Vestovoj Dimo.txt',
                    'data/BulTreeBank/processed/Girltalk.txt',
                    'data/BulTreeBank/processed/Ivan Vazov Chichovtzi.txt',
                    'data/BulTreeBank/processed/Robert Sheckley Skulking Permit.txt',
                    'data/BNC/processed/JOURNALISM.BG/C-MassMedia/C-Culture/C-Culture.txt',
                    'data/BNC/processed/JOURNALISM.BG/C-MassMedia/D-Society/D-Society.txt',
                    'data/BNC/processed/JOURNALISM.BG/C-MassMedia/E-Economy/E-Economy.txt',
                    'data/BNC/processed/JOURNALISM.BG/C-MassMedia/J-Politics/J-Politics.txt',
                    'data/BNC/processed/JOURNALISM.BG/C-MassMedia/S-Military/S-Military.txt']

with open(duplicate_sentences_file_name, "w") as duplicate_sentences_file:
    for input_file_name in input_file_names:
        with open(input_file_name, "r") as input_file:
            input_file_contents = input_file.read().splitlines()

        with open(input_file_name, "w") as input_file:
            for line in input_file_contents:
                if line not in sentences_seen:
                    print(line, file=input_file)
                    sentences_seen.add(line)
                else:
                    print(input_file_name, line, file=duplicate_sentences_file)
