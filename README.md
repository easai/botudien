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

vi-flash.py -- Vietnamese flash cards
<pre>
Usage: vi-flash.py [--help|-h] [--local|-l] [-n N]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
</pre>

vi-quiz.py -- Vietnamese vocabulary quiz.
<pre>
Usage: vi-quiz.py [--help|-h] [--local|-l] [-n N] [-m M]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
</pre>
A sample session would look as follows:
<pre>
1: draw
2: a sheet of paper
3: one
4: he
5: apple
Which best describes the word [vẽ]? 1
Correct.
[vẽ] means [draw]
</pre>

vi-write.py -- Vietnamese vocabulary quiz (type in the word).
<pre>
Usage: vi-write.py [--help|-h] [--local|-l] [-n N] [-m M] [--pause|-p PAUSE]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
    -p, --pause PAUSE  number of seconds before going on
</pre>
A sample session would look as follows:
<pre>
Which of the following words best describes [mug]?
tò giấy
găng tay
thư
ca
ngã
Enter the word: ca
Correct.
[ca] means [mug]
</pre>
