import json
from typing import Union
from os.path import dirname, abspath

filename = 'morse_tables.json'

try:
    with open(filename) as json_file:
        PATTERNS = json.load(json_file)
except FileNotFoundError:
    raise SystemExit(f"""
File ‘{filename}’ not found at {abspath(dirname(__file__))}

You can download a copy of this file here:
    https://github.com/willy-r/morse-translator/blob/main/morse_tables.json""")


def get_morse_code(char: str) -> str:
    return PATTERNS['to'].get(char.lower(), '#')


def get_char(morse_code: str) -> str:
    return PATTERNS['from'].get(morse_code, '#')


def get_sound_path(char: str) -> Union[str, None]:
    return PATTERNS['sounds'].get(char)
