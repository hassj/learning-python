#!/usr/bin/env python3.8

import argparse
import sys

#Creating a class
parser = argparse.ArgumentParser(description='Read a file in reverse')

#Calling add_argument method
parser.add_argument('filename', help='the file to read')
parser.add_argument("--version", "-v", action="version", version='%(prog)s 2.0')
parser.add_argument("--limit", "-l", type=int, help="the line to read")

#Calling the parse_args()
args = parser.parse_args()

#using try excep else block
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"{err}")
    sys.exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

    if limit:
        lines = lines[:limit]
    
    for line in lines:
        print(line.strip()[::-1])

