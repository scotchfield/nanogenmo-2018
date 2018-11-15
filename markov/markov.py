import random
import sys

WORD_COUNT = 50

next = {}

def tokenize(data):
    data = data.replace('\n', ' ')
    while data.find('  ') > -1:
        data = data.replace('  ', ' ')
    data = data.strip()
    tokens = data.split(' ')

    for i in range(len(tokens) - 1):
        token = tokens[i]
        next[token] = next.get(token, [])
        next[token].append(tokens[i + 1])

if __name__ == "__main__":
    VERBOSE = True

    try:
        input_filename = sys.argv[1]
    except IndexError:
        print('Please pass the filename as an argument. For example:')
        print('> python parser.py stories/simple.txt')
        sys.exit(1)

    input_file = open(input_filename, 'r')
    data = input_file.read()

    tokenize(data)

    output = []
    last = None
    while len(output) < WORD_COUNT:
        word = None
        if last is None:
            word = random.choice(next.keys())
        else:
            word = random.choice(next[last])
        output.append(word)
        last = word

    print ' '.join(output)
