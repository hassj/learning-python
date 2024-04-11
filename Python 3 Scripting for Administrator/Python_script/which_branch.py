#!/usr/bin/env python3.8

import os

# this version will use os.environ function 

stage = os.environ['STAGE'].upper()
output = f"Your running on {stage}"

if stage.startswith('PROD'):
    output = print(f"You're running on PRODUCTION branch !!!! DANGER")
print(output)