"""Vietnamese online dictionary.

Usage: vi.py [--help|-h][--local|-l][--vi|-v] <word>

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -v, --vi  the word is in Vietnamese
"""
import requests
from docopt import docopt
import time
from botudien import *


def vi(word, lang=None, is_local=False):
    try:
        botudien = Botudien(is_local=is_local)
        if not lang:
            lang = 'en'
        res = botudien.lookup(lang, word)
        n = len(res)
        if type(res) is list:
            for item in res:
                sana = Sana(item)
                print(sana)
        else:
            print('That is not in my dictionary (sorry!).')
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    args = docopt(__doc__)
    lang = None
    if args["--vi"]:
        lang = 'vi'
    vi(args['<word>'], lang, is_local=args['--local'])
