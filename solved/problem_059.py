import time

with open(r'p059_cipher.txt', 'r') as f:
    raw_input = f.read()

nrs = [int(i) for i in raw_input.strip().split(',')]

def decrypt(keys, inputs):
    txt = ""
    for idx in range(0, len(inputs)):
        txt += chr(inputs[idx] ^ keys[idx%3])
    return txt

def ascii_sum(text):
    return sum([ord(x) for x in text])

min_ = ord('a')
max_ = ord('z')

for one in range(min_, max_+1):
    for two in range(min_, max_+1):
        for three in range(min_, max_+1):
            text = decrypt([one, two, three], nrs)

            if 'Euler' in text:
                print(one, two, three, text)
                print(ascii_sum(text))
                break
