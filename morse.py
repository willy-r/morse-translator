from playsound import playsound

from cli import get_args
from utils import get_morse_code, get_char, get_sound_path


def to_morse(text: str) -> str:
    """Translate normal text to Morse Code."""
    morse_code = []
    for chars in text.split():
        for char in set(chars):
            code = get_morse_code(char)
            chars = chars.replace(char, f'{code} ')
        morse_code.append(chars)
    return '/ '.join(morse_code).rstrip()


def from_morse(morse_code: str) -> str:
    """Translate Morse Code to normal text."""
    text = []
    for morse_word in morse_code.split(' / '):
        codes = morse_word.split()
        for i, code in enumerate(codes):
            char = get_char(code)
            codes[i] = char
        text.append(''.join(codes))
    return ' '.join(text).upper()


def morse_code_sound(morse_code: str) -> None:
    """Play sound for Morse Code."""
    for code in morse_code:
        path = get_sound_path(code)
        if path is not None:
            playsound(path)


def main() -> None:
    args = get_args()
    if args._to is not None:
        result = to_morse(args._to)
        print(result)
        if args.sound:
            morse_code_sound(result)
    else:
        print(from_morse(args._from))
        if args.sound:
            morse_code_sound(args._from)


if __name__ == '__main__':
    main()
