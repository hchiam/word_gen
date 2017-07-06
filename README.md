# Markov Word Generator

The original inspiration for this project:

Original video (en français): https://www.youtube.com/watch?v=YsR7r2378j0

Original code: https://sciencetonnante.wordpress.com/2015/10/16/la-machine-a-inventer-des-mots-video/

## Use It:

Install Python2 or Python3, `numpy`, and `click`. New Macs come with Python2 installed.

Then run this command in Terminal/CLI/Bash (you'll have to wait a little while it processes your data):

`python make_map.py && python create_words.py`

(The `&&` runs the second command only if the first command works.)

Input data file: `input.txt`. Put at least about 30 words here to have the algorithm working, but maybe over a thousand to get more robust/realistic results. You can get real word lists from the Gutenberg project.

Output data file: `output.txt`. See your words get generated here! :)

(You can re-run `python create_words.py` multiple times if you didn't reset the input words.)
