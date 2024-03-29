"""Vietnamese vocabulary quiz (type in the word).

Usage: vi-write.py [--help|-h] [--local|-l] [-n N] [-m M] [--pause|-p PAUSE]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
    -p, --pause PAUSE  number of seconds before going on
"""
from docopt import docopt
import random
import unidecode
import time
from botudien import *

wrong = []
pause = 3


def quiz(n=10, n_choices=5, is_local=False):
    try:
        botudien = Botudien(is_local=is_local)
        n_words = int(n)
        for i in range(n_words):
            res = botudien.nrand(n_choices)
            n = len(res)
            r = random.randrange(0, n)
            ans = Sana(res[r])
            print(f"Which of the following words best describes [{ans.desc}]?")
            for j in range(n_choices):
                opt = Sana(res[j])
                print(f"{opt.exp}")
            try:
                choice = input("Enter the word: ").strip()
                if unidecode.unidecode(choice) == unidecode.unidecode(ans.exp):
                    print(f"Correct.")
                else:
                    wrong.append(ans)
                    print(f"Incorrect.")
            except KeyboardInterrupt:
                exit(0)
            except Exception as e:
                wrong.append(ans)
            print(ans)
            time.sleep(pause)
            print()
        if wrong:
            print("Review the following word(s):")
            botudien.dump(wrong)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    args = docopt(__doc__)
    n = 10
    m = 5
    if args["-n"]:
        try:
            n = int(args['-n'])
        except ValueError:
            print("N must be an integer")
    if args['-m']:
        try:
            m = int(args['-m'])
        except ValueError:
            print("M must be an integer")
    if args['--pause']:
        try:
            pause = int(args['--pause'][0])
        except ValueError:
            print("PAUSE must be an integer")
    quiz(n, m, is_local=args["--local"])
