import sys

from utils import get_pattern


def to_morse(sentence: str) -> str:
    morse_sentence = []
    for chars in sentence.split():
        for char in set(chars):
            code = get_pattern(char, search_key='to')
            chars = chars.replace(char, f'{code} ')
        morse_sentence.append(chars)
    return '/ '.join(morse_sentence)


def from_morse(morse_sentence: str) -> str:
    sentence = []
    for morse_word in morse_sentence.split(' / '):
        codes = morse_word.split()
        for i, code in enumerate(codes):
            char = get_pattern(code, search_key='from')
            codes[i] = char
        sentence.append(''.join(codes))
    return ' '.join(sentence).upper()


if __name__ == '__main__':
    phrase = sys.argv[1]
    print(to_morse(phrase))
    print(from_morse(phrase))
