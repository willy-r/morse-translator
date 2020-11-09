# morse-translator

A simple [Morse Code](https://en.m.wikipedia.org/wiki/Morse_code) translator written in Python.

---

## Instalation

- You need Python 3.9 installed in your computer.

### Clone

- Clone this repo to your local machine using `https://github.com/willy-r/morse-translator`

### Setup

- Go to `morse-translator` directory:

```shell
$ cd morse-translator
```

---

## Usage

To translate normal text to Morse Code use:

```shell
$ python morse.py -t TEXT
```

- TEXT is a normal text surrounded by **'** or **"**.

To translate Morse Code to text use:

```shell
$ python morse.py -f MORSE
```

- MORSE is a Morse Code surrounded by **'** or **"**, using '.' or '-', separating letters by spaces and words by '/'.

> **Note**: If the pattern for both options is not in the [patters.json](https://github.com/willy-r/morse-translator/blob/main/patterns.json) file, the pattern will be replaced with '#'.

Enter `$ python morse.py -h` to see more commands.

---

## Example

- To Morse Code examples:

```shell
$ python morse.py -t 'morse code!'
-- --- .-. ... . / -.-. --- -.. . -.-.--

$ python morse.py -t morse
-- --- .-. ... .

$ python morse.py -t 1999
.---- ----. ----. ----.

$ python morse.py -t 'maçã'
-- .- # #
```

- From Morse Code examples:

```shell
$ python morse.py -f '-- --- .-. ... . / -.-. --- -.. . -.-.--'
MORSE CODE!

$ python morse.py -f '-- --- .-. ... .'
MORSE

$ python morse.py -f '.---- ----. ----. ----.'
1999

$ python morse.py -f '-- .- # #'
MA##
```

---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/willy-r/morse-translator`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/willy-r/morse-translator/compare" target="_blank">`https://github.com/willy-r/morse-translator/compare`</a>.

---

# Support

Reach out to me at one of the following places!

- Twitter at <a href="https://twitter.com/lliw_r?s=09" target="_blank">`@lliw_r`</a>

---
