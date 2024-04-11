#!/usr/bin/env python3.8

import argparse

#Creating class argumentparser
parser = argparse.ArgumentParser(description="Read a file in reverse")
# Calling add_argument method
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of line to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

# Calling parse_args() method
args = parser.parse_args()
#reverse content of a line
with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()
    
if args.limit:
    lines = lines[:args.limit] 

for line in lines:
    print(line.strip()[::-1])