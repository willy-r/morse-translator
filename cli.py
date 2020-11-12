import argparse


def get_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(prog='morse',
                                description='Translate to and from Morse Code')
    p.version = '1.1.0'
    g = p.add_mutually_exclusive_group(required=True)

    p.add_argument('-v',
                   '--version',
                   action='version')

    p.add_argument('-s',
                   '--sound',
                   action='store_true',
                   help='play sound for the Morse Code')

    g.add_argument('-t',
                   '--to',
                   action='store',
                   metavar='TEXT',
                   dest='_to',
                   help='translate normal TEXT to morse')

    g.add_argument('-f',
                   '--from',
                   action='store',
                   metavar='MORSE',
                   dest='_from',
                   help=('translate MORSE (using "." or "-", separating '
                         'letters by spaces and words by "/") to text'))
    return p.parse_args()
