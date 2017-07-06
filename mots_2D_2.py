#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import numpy as np
from numpy.random import choice, seed
import codecs # so can use special characters

import sys
PY3 = (sys.version_info[0] >= 3)

if PY3:
    unichr = chr

def process(codec, random_seed):
    if random_seed:
        seed(None)
    else:
        seed(1)
    filepath = 'input.txt'
    outfile = 'output.txt'
    probafile = 'counts.bin'

    dico = []
    with codecs.open(filepath, "r", "ISO-8859-1") as lines:
        for l in  lines:
            dico.append(l[:-1])

    count = np.fromfile(probafile, dtype="int32").reshape(256,256,256)

    s = count.sum(axis=2)
    st = np.tile(s.T, (256,1,1)).T
    p = count.astype('float') / st
    p[np.isnan(p)] = 0

    with codecs.open(outfile, "w", codec) as f:
        outputexamples = 30 # originally: 100
        maxwordlength = 10
        for TGT in range(maxwordlength,maxwordlength+1): # originally: for TGT in range(12,13):
            total = 0
            while total < outputexamples:
                i = 0
                j = 0
                res = u''
                while not j==10:
                    k=choice(range(256),1,p=p[i,j,:])[0]
                    #res = res + chr(k)
                    res = res + unichr(k)
                    i = j
                    j = k
                if len(res) == 1 + TGT:
                    x = res[:-1]
                    if res[:-1] in dico:
                        x = res[:-1] + "*"
                    total += 1
                    print(x)
                    f.write(x + "\n")

def main(codec='ISO-8859-1', random_seed=True):
    if random_seed:
        print("Using a truly random seed")
        print("Use --no-random-seed to get reproducible results")
    process(codec, random_seed=random_seed)

if __name__ == '__main__':
    main()
