from utils import get_pattern, get_args


def to_morse(text: str) -> str:
    """Translate normal text to Morse Code."""
    morse_code = []
    for chars in text.split():
        for char in set(chars):
            code = get_pattern(char, search_key='to')
            chars = chars.replace(char, f'{code} ')
        morse_code.append(chars)
    return '/ '.join(morse_code)


def from_morse(morse_code: str) -> str:
    """Translate Morse Code to normal text."""
    text = []
    for morse_word in morse_code.split(' / '):
        codes = morse_word.split()
        for i, code in enumerate(codes):
            char = get_pattern(code, search_key='from')
            codes[i] = char
        text.append(''.join(codes))
    return ' '.join(text).upper()


def main() -> None:
    args = get_args()
    if args._to is not None:
        print(to_morse(args._to))
    else:
        print(from_morse(args._from))


if __name__ == '__main__':
    main()
