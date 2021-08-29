import sys
import re


input_file_name = sys.argv[1]
statistics_file_name = re.sub('\.txt', '_mismatched_sentences.txt', input_file_name)

with open(input_file_name,"r") as input_file:
    input_file_contents = input_file.read().splitlines()

with open(statistics_file_name,"w") as statistics_file, open(input_file_name,"w") as input_file:
    for line_number, line in enumerate(input_file_contents):
        line = line.rstrip('\n')
        count = 0

        for char in line:
            if char == ")":
                count -= 1
            elif char == "(":
                count += 1
            if count < 0:
                break

        if line.startswith('"') and line.endswith('"') and line.count('"') == 2 or line.startswith('(') and line.endswith(')') or count != 0 or line.count('"') % 2 != 0:
            print(line_number, ':', line, file=statistics_file)

            line_without_enclosing_quotation_marks = re.sub('^"(.*)"$', '\\1', line)
            line_without_enclosing_brackets = re.sub('^\((.*)\)$', '\\1', line_without_enclosing_quotation_marks)

            line_with_closed_opening_quotation_marks = re.sub('("[^"]+[.!?])', '\\1"', line_without_enclosing_brackets)
            line_without_enclosing_quotation_marks = re.sub('^"(.*)"$', '\\1', line_with_closed_opening_quotation_marks)
            line_with_closed_opening_brackets = re.sub('(\([^)]+[.!?])', '\\1)', line_without_enclosing_quotation_marks)
            line_without_enclosing_brackets = re.sub('^\((.*)\)$', '\\1', line_with_closed_opening_brackets)

            line_without_unopened_closing_quotation_marks = re.sub('^([^"]*)([?!.])"', '\\1\\2', line_without_enclosing_brackets)
            line_without_unopened_closing_quotation_marks = re.sub('^([^"]*)"([.!?])', '\\1\\2', line_without_unopened_closing_quotation_marks)
            line_without_unopened_closing_brackets = re.sub('^([^(]*)([?!.])\)', '\\1\\2', line_without_unopened_closing_quotation_marks)
            line_without_unopened_closing_brackets = re.sub('^([^(]*)\)([.!?])', '\\1\\2', line_without_unopened_closing_brackets)
            line_without_enclosing_quotation_marks = re.sub('^"(.*)"$', '\\1', line_without_unopened_closing_brackets)
            line = re.sub('^\((.*)\)$', '\\1', line_without_enclosing_quotation_marks)
            
        print(line, file=input_file)


