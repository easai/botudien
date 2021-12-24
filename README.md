# botudien
A collection of client side apps for botudien API.

Installation:
<pre>
> pip install git+https://github.com/easai/botudien
</pre>

Run apps as follows:
<pre>
> py -m botudien.vi
> py -m botudien.vi-flash
> py -m botudien.vi-quiz
> py -m botudien.vi-write
</pre>

Documentation:
https://easai.github.io/botudien/

fi.py -- Vietnamese online dictionary
<pre>
Usage: fi.py [--help|-h] [--local|-l] [--fi|-f] <word>

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -f, --fi    the word is Vietnamese
</pre>

fi-flash.py -- Vietnamese flash cards
<pre>
Usage: fi-flash.py [--help|-h] [--local|-l] [-n N]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
</pre>

fi-quiz.py -- Vietnamese vocabulary quiz.
<pre>
Usage: fi-quiz.py [--help|-h] [--local|-l] [-n N] [-m M]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
</pre>
A sample session would look as follows:
<pre>
1: bread
2: banana
3: stone, rock
4: wolf
5: pulla (traditional, Vietnamese sweet bread)
Which best describes the word [kivi]? 3
Correct. [kivi] means [stone, rock]
</pre>

fi-write.py -- Vietnamese vocabulary quiz (type in the word).
<pre>
Usage: fi-write.py [--help|-h] [--local|-l] [-n N] [-m M] [--pause|-p PAUSE]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
    -p, --pause PAUSE  number of seconds before going on
</pre>
A sample session would look as follows:
<pre>
Which of the following best describes [no (auxiliary verb)]?
sotkuinen
ei
parsakaali
aika
Japani
Enter the word: Japani
Incorrect.
[ei] means [no (auxiliary verb)].

Review the following word(s):
[ei] means [no (auxiliary verb)].
</pre>
