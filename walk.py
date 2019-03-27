#!/usr/bin/env python3

# This script returns a list of all files matching a certain filetype
# that are contained within a certain directory. Uses command-line
# arguments to specify the directory and filetype.

import os
import argparse

parser = argparse.ArgumentParser(description='Finds all files of a specified \
        filetype within the specified directory')
parser.add_argument('folder', help='Directory to search')
parser.add_argument('type', help='Filetype to look for')
args = parser.parse_args()
f = os.walk(args.folder)
filenames = []

for path, dir, files, in f:
    for file in files:
        if (file.endswith(args.type)):
            filenames.append(file)
for i in filenames:
    print(i)
