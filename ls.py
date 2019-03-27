#!/usr/bin/env python3

# This silly script reimplements the bash command "ls -al"

import subprocess as sub

f = sub.Popen(['ls', '-al'], stdout = sub.PIPE)
print(f.communicate())
