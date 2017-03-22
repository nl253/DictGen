#!/usr/bin/python
from pathlib import Path
import itertools
import re
from collections import Counter
from argparse import ArgumentParser
from pprint import pprint
parser = ArgumentParser(description='Generate a dictionary from a file.')
parser.add_argument('text_files', nargs='+', type=str)
parser.add_argument('--output', help='the file where the dict should be written')
args = parser.parse_args()
files = args.text_files
paths = [Path(i) for i in files if Path(i).exists() and Path(i).is_file()]
texts = [inputFile.read_text() for inputFile in paths]
text = "".join(texts)
pattern = re.compile("\w+", flags=re.MULTILINE)
matchesDict = Counter(pattern.findall(text))
# WORD : WORD FREQ
[print(i) for i, j in Counter(matchesDict).most_common(10000) if len(i) > 3 and len(i) < 16]
