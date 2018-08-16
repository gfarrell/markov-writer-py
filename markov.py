import numpy
from numpy.random import choice

SPEECH_START = "$$$SPEECH_START$$$"
SPEECH_END = "$$$SPEECH_END$$$"

def generate_pairs(speech):
    """Generates pairs of words to indicate what follows what"""
    words = [word.lower() for word in speech.split(" ")]
    bookends = [(SPEECH_START, words[0]), (words[-1], SPEECH_END)]
    return bookends + [(word, words[i + 1]) for i, word in enumerate(words[:-1])]

def normalise(matrix):
    return [
        [x / t if t > 0 else 0.0 for x in row]
        for row, t in
            ((row, sum(row))
                for row in matrix
            )
    ]

def generate_matrix(speeches):
    """Generates a transition matrix"""
    pairs = [pair for speech in speeches for pair in generate_pairs(speech)]
    words = { word: index for index, word in enumerate(list(sorted(set([pair[0] for pair in pairs] + [SPEECH_END])))) }
    matrix = numpy.zeros(shape=(len(words), len(words)))

    for (a, b) in pairs:
        matrix[words[a]][words[b]] += 1

    return words, normalise(matrix)

def transition(word, words, matrix):
    """Generate the next word"""
    return choice(list(words.keys()), p=matrix[words[word]])

def write_like_this(speeches):
    """Generate a body of text given input text"""
    words, matrix = generate_matrix(speeches)
    output = [SPEECH_START]
    while output[-1] != SPEECH_END:
        output.append(transition(output[-1], words, matrix))
    return " ".join(output[1:-1])
