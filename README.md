# Markov Word Generator

See here for the original inspiration for this project:

Original video (en français): https://www.youtube.com/watch?v=YsR7r2378j0

Original code: https://sciencetonnante.wordpress.com/2015/10/16/la-machine-a-inventer-des-mots-video/

## Usage

Install Python2 or Python3 with `numpy` and `click`.

Then run this command (you'll have to wait a little):

`python mots_2D.py && python mots_2D_2.py`

(The `&&` runs the second command only if the first command works.)

Input data file: `input.txt`. Put at least about 30 words here to have the algorithm working, but maybe over a thousand to get more robust/realistic results.

Output data file: `output.txt`. See your generated words here! :)

(You can re-run `python mots_2D_2.py` multiple times if you didn't reset the input words.)

You can choose the language with ``--lang`` and the encoding with
``--codec``
