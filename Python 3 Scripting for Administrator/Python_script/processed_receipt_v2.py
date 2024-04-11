#!/usr/bin/env python3.8

import os
import glob
import shutil
import json

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exist")

subtotal = 0.0

#Get a lists of receipts use glob.glob method
receipts = glob.glob('./new/receipt-[0-9].json')
subtotal = 0.0

#read file and translate it to python object of dictionary
for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    dest = path.replace('new', 'processed')
    shutil.move(path, dest)
    print(f"move '{path} to {dest}")
print(f"subtotal: ${round(subtotal, 2)}")