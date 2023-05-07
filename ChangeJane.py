#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        oldname = line.strip()
        newname = oldname.replace('jane', 'jdoe')
        subprocess.run(['mv', oldname, newname])

print('All done!')
