#!/usr/bin/python

# This script recurses through the named directory and renames all files that
# match the pattern

import os

def main():

    directory = "/home/ad_app_c.calhoun/pe2020Cloud"
    old = "oimt-adtpe2018"
    new = "oimt-pe2020Cloud"

    for (paths, dirs, files) in os.walk(directory):
        for f in files:
            # The full path must be specified for the rename to work
            src = os.path.join(paths, f)
            dest = os.path.join(paths, f.replace(old, new))
            os.rename(src, dest)


if __name__ == '__main__':
    main()

# Here is the find command I used for uploading:
# find pe2020Cloud/ -type f -name *ls? -exec java -jar adijar.jar upload {} \;
