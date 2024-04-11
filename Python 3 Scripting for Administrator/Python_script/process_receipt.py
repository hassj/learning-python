#!/usr/bin/env python3.8

import os
import glob
import json
import shutil


try:
    os.mkdir('./processed')
except OSError: 
    print("'processed' directory already exist")

#Get a lists of receipts use glob.glob method
receipts = glob.glob('./new/receipt-[0-9].json')
subtotal = 0.0

#read file and translate it to python object of dictionary
for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    dest = f"./processed/{name}"
    shutil.move(path, dest)
    print(f"move '{path} to {name}")
print("Subtotal: $%.2f" %subtotal)