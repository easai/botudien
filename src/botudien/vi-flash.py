"""vietnamese flash cards

Usage: vi-flash.py [--help|-h] [--local|-l] [-n N]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
"""
import requests
from docopt import docopt
from botudien import *


def vi(n=10, is_local=False):
    botudien = Botudien(is_local=is_local)
    try:
        index = botudien.nrand(n)
        for i in range(n):
            sana = Sana(index[i])
            input(f"{sana.exp}?")
            print(f"{sana.exp}: {sana.desc}")
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    args = docopt(__doc__)
    n = 10
    if args["-n"]:
        try:
            n = int(args['-n'])
        except ValueError:
            print("n must be an integer")
    vi(n, is_local=args["--local"])
