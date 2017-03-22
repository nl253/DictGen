#!/usr/bin/python
# -*- coding: utf-8 -*-
from pathlib import Path
import itertools
import re
from collections import Counter
from pprint import pprint
books = [
    'HarryPotter1.txt',
    'HarryPotter2.txt'
    'HarryPotter3.txt'
    'HarryPotter4.txt'
    'HarryPotter5.txt'
    'HarryPotter6.txt'
    'HarryPotter7.txt'
    'AliceInWonderland.txt',
    'bash_man.txt',
    'find_man.txt',
    'computer_science_textbook.txt',
    'emacs_man.txt',
    'python_textbook.txt',
    'set_theory_cs.txt',
    'maths_for_cs.txt',
    'think_like_a_cs.txt',
]
inputFiles = [Path(i) for i in books if Path(i).exists() and Path(i).is_file()]
texts = [inputFile.read_text() for inputFile in inputFiles]
text = "".join(texts)
pattern = re.compile("\w+", flags=re.MULTILINE)
matchesDict = Counter(pattern.findall(text))
# print(matchesList)
# WORD : WORD FREQ
# [print(i) for i in matchesDict]
[print(i) for i, j in Counter(matchesDict).most_common(10000)]
# coding=utf-8
#

