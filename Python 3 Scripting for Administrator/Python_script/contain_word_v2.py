#!/usr/bin/env python3.8

import argparse

parser = argparse.ArgumentParser(description="finding word including in words")
parser.add_argument("snippet", help='partial or full string')
args = parser.parse_args()

snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()

print([word.strip() for word in words if snippet in word.lower()])