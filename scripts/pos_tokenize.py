import classla
import sys
import json
import re


input_file_name = sys.argv[1]

with open(input_file_name, "r") as input_file:
    input_file_contents = input_file.read().splitlines()

nlp = classla.Pipeline('bg', processors='tokenize,pos')

pos_input_file_contents = [nlp(sentence).to_dict()[0][0] for sentence in input_file_contents]

output_file_name = re.sub('\.txt', '.json', input_file_name)

with open(output_file_name, "w") as output_file:
    json.dump(pos_input_file_contents, output_file)
    
