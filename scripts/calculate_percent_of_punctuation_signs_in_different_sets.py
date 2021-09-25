# arguments are:
# sys.argv[1]: the name of the original file divided into train, dev, test (and rest)
# outcome:
# prints on the screen the percentages for the different punctuation signs in the three sets and in the original file

import sys
import re
from string import punctuation
from collections import Counter


punctuation_enhanced = punctuation + '\n–„“…'

input_file_name = sys.argv[1]
train_file_name = re.sub('\.txt', '_train.txt', input_file_name)
dev_file_name = re.sub('\.txt', '_dev.txt', input_file_name)
test_file_name = re.sub('\.txt', '_test.txt', input_file_name)

counts = Counter(open(input_file_name).read())    
input_file_punctuation_counts = {k:v for k, v in counts.items() if k in punctuation_enhanced}
print(input_file_name, ':', input_file_punctuation_counts)

for file_name in (train_file_name, dev_file_name, test_file_name):
    counts = Counter(open(file_name).read())    
    percent_of_input_file_punctuation_counts = {k:round(v/input_file_punctuation_counts[k]*100, 2) for k, v in counts.items() if k in punctuation_enhanced}
    print(file_name, ':', percent_of_input_file_punctuation_counts)


