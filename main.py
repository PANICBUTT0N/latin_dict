import re
import csv

# Allow user to decide if they want the gender field written as a full word or a single letter abbreviation.


def word():
    func_dict = {'- m.': 'masculine',
                 '- n.': 'neuter',
                 '- f.': 'feminine'}
    filename = r'output\latin_output_word.csv'
    return func_dict, filename


def abbreviations():
    func_dict = {'- m.': 'm.',
                 '- n.': 'n.',
                 '- f.': 'f.'}
    filename = r'output\latin_output_abbrev.csv'
    return func_dict, filename


while True:
    match input('Write genders as full words or abbreviations? (word, abbrev)\n'):
        case 'word':
            gender_replacements, filename = word()
            break
        case 'abbrev':
            gender_replacements, filename = abbreviations()
            break
        case _:
            print('Invalid input.')

with open('str.txt', 'r', encoding='utf-8') as read:
    # Entries in the dictionary are separated by carets. This makes each line an
    # individual entry. Also removes problematic formatting.
    content = [line.lstrip().replace('*', '').replace('{gen.}', 'gen.').replace
               (', ', '- ').replace('$', ',').replace('%', '').replace
               ('pl.', ' pl.') for line in read.read().split('^')]
content = [line.split(',') for line in content]

# Find gender values present in word column cells and moves them to discrete cells if present. If not present, empty
# cell is created to normalize formatting.
entries = []
for entry in content:
    modified_entry = entry
    gender_present = any(gender in modified_entry[0] for gender in gender_replacements.keys())
    if gender_present:
        for gender, replacement in gender_replacements.items():
            if gender in modified_entry[0]:
                modified_entry[0] = modified_entry[0].replace(gender, '')
                modified_entry.insert(1, replacement)
                break
    else:
        modified_entry.insert(1, '')
    entries.append(modified_entry)

# If word definitions reference other words, input the referenced word and its definition into the definition field.
# Additionally, provide the row index of the referenced entry.
for row_index, row_contents in enumerate(entries):
    row_contents.insert(0, str(row_index))
    if '[' in row_contents[3]:
        match_value = re.findall(r'\[(.*?)]', row_contents[3])[0]
        for row_index1, row_contents1 in enumerate(entries):
            if match_value in row_contents1[1]:
                row_contents[3] = f'{row_contents1[1]} ({row_contents1[3]})'
                row_contents.append(f'See entry index: {row_contents1[0]}')
                break
    else:
        row_contents.append('')
    # Re-introduce commas to separate words in word and definition fields, now without messing with CSV formatting.
    row_contents[1] = row_contents[1].replace('-', ',')
    row_contents[3] = row_contents[3].replace('-', ',')

with open(filename, 'w', newline='', encoding='utf-8') as write:
    writer = csv.writer(write)
    writer.writerow(['Index', 'Latin Word', 'Gender', 'Definition', 'Reference Entry Index'])
    writer.writerows(entries)
