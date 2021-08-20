import os
from string import punctuation
from collections import Counter


punctuation_enhanced = punctuation + '\n–„“…'
file_names = ['Bible/processed/Bibliia_clean.txt',
              'BulTreeBank/processed/Atanas Dalchev Fragments.txt',
              'BulTreeBank/processed/Ladislav Klima Novel.txt',
              'BulTreeBank/processed/Bulgarian parliament Meetings.txt',
              'BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 1.txt',
              'BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 2.txt',
              'BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 3.txt',
              'BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 4.txt',
              'BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 5.txt',
              'BulTreeBank/processed/Bulgarian parliament Recorded Sessions – part 7.txt',
              'BulTreeBank/processed/Bulgarian President News – part 1.txt',
              'BulTreeBank/processed/Bulgarian President News – part 2.txt',
              'BulTreeBank/processed/Bulgarian President News – part 3.txt',
              'BulTreeBank/processed/Bulgarian President News – part 4.txt',
              'BulTreeBank/processed/Bulgarian President News – part 5.txt',
              'BulTreeBank/processed/Georgi Stamatov Vestovoj Dimo.txt',
              'BulTreeBank/processed/Girltalk.txt',
              'BulTreeBank/processed/Ivan Vazov Chichovtzi.txt',
              'BulTreeBank/processed/Robert Sheckley Skulking Permit.txt',
              'BNC/processed/JOURNALISM.BG/C-MassMedia/C-Culture/C-Culture.txt',
              'BNC/processed/JOURNALISM.BG/C-MassMedia/D-Society/D-Society.txt',
              'BNC/processed/JOURNALISM.BG/C-MassMedia/E-Economy/E-Economy.txt',
              'BNC/processed/JOURNALISM.BG/C-MassMedia/J-Politics/J-Politics.txt',
              'BNC/processed/JOURNALISM.BG/C-MassMedia/S-Military/S-Military.txt',]

accumulated_counts = Counter({})

for file_name in file_names:
    dir_name = os.path.dirname(__file__)
    full_file_name = os.path.join(dir_name, file_name)

    counts = Counter(open(full_file_name).read())    
    punctuation_counts = {k:v for k, v in counts.items() if k in punctuation_enhanced}
    print(full_file_name, ':', punctuation_counts)

    accumulated_counts.update(Counter(punctuation_counts))

print('All:', dict(accumulated_counts))

