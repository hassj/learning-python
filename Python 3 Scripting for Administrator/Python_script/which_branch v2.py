#!/usr/bin/env python3.8

import os

# this version will use os.getenv function 

stage = os.getenv('STAGE', 'DEV')
output = f"Your running on {stage}"

if stage.startswith('PROD'):
    output = print(f"You're running on PRODUCTION branch !!!! DANGER")
print(output)