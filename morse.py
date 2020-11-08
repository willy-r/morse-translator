import sys

from utils import get_code, get_letter


def to_morse(sentence):
    morse_sentence = []
    for word in sentence.split():
        for letter in set(word):
            code = get_code(letter)
            if code is not None:
                word = word.replace(letter, f'{code} ')
        morse_sentence.append(word)
    return '/ '.join(morse_sentence)


def from_morse(morse_sentence):
    sentence = []
    for morse_word in morse_sentence.split(' / '):
        codes = morse_word.split()
        for i, code in enumerate(codes):
            letter = get_letter(code)
            if letter is not None:
                codes[i] = letter
        sentence.append(''.join(codes))
    return ' '.join(sentence).upper()


if __name__ == '__main__':
    phrase = sys.argv[1]
    print(to_morse(phrase))
    print(from_morse(phrase))
