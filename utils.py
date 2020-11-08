import json
from os.path import dirname, abspath

filename = 'patterns.json'

try:
    with open(filename) as json_file:
        PATTERNS = json.load(json_file)
except FileNotFoundError:
    raise SystemExit(f"""
File ‘{filename}’ not found at {abspath(dirname(__file__))}

You can download a copy of this file here:
    https://gist.github.com/willy-r/ff931189e7ad33f85e21ca01130072be""")


def get_pattern(pattern: str, *, search_key: str) -> str:
    if search_key not in ['to', 'from']:
        raise KeyError('Not a valid key, enter ‘to’ or ‘from’')
    return PATTERNS[search_key].get(pattern.lower(), '#')
