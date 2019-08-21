import re
import datetime
import time

now = datetime.datetime.now
now = time.time

start = now()

with open(r'p089_roman.txt', 'r') as f:
    raw_input = f.read()

inputs = raw_input.strip().split("\n")

def check_roman_numerals(text):
    new = text + ""
    new = re.sub('VIIII', 'IX', new)
    new = re.sub('IIII', 'IV', new)
    new = re.sub('LXXXX', 'XC', new)
    new = re.sub('XXXX', 'XL', new)
    new = re.sub('DCCCC', 'CM', new)
    new = re.sub('CCCC', 'CD', new)
    return new

def get_full_length(inputs):
    return sum([len(line) for line in inputs])


pre = get_full_length(inputs)

for idx in range(len(inputs)):
    inputs[idx] = check_roman_numerals(inputs[idx])

post = get_full_length(inputs)

print(pre, post, pre-post)

print(now()-start)