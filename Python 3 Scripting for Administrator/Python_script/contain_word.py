#!/usr/bin/env python3.8

import argparse

parser = argparse.ArgumentParser(description="finding word including in words")
parser.add_argument("snippet", help="partial")
args = parser.parse_args()

snippet = args.snippet.lower()

matches = []

with open('/usr/share/dict/words') as f:
    words = f.readlines()

for word in words:
        if snippet in word.lower():
            matches.append(word)
print(matches)
