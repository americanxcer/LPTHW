
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',

    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',

    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',

    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',

    1 : 'number',
    2 : 'number',
    3 : 'number',
    4 : 'number',
    5 : 'number',
    6 : 'number',
    7 : 'number',
    8 : 'number',
    9 : 'number',
            }

stuff = raw_input('> ')
words = stuff.split()

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('drection', 'west')
sentence = [first_word, second_word, third_word]

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        pair = (lexicon[word], word)
        result.append(pair)

    return result
