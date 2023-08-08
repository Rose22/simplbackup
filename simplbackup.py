#!/usr/bin/env python

# simplbackup: takes a list of folders to back up, copies them all into one folder into your specified structure and then zips the whole thing up and optionally sends it to a cloud service

# example config file:
"""
backup.{date}.zip

/home/user/.retroarch : emulation/retroarch
/home/user/.config/dolphin : emulation/dolphin
/home/user/.config/emulationstation : emulation/ES
"""
# will copy /home/user/.retroarch to emulation/retroarch inside the zip file, and so on.

import os
import sys
import shutil
from datetime import datetime

TMPDIR = "/tmp/simplbackup/"

if not sys.argv[1]:
    print("please provide an input file")
    sys.exit()

inputfile = sys.argv[1]

if not os.path.exists(inputfile):
    print("file does not exist")
    sys.exit(1)

configlines = []
with open(inputfile, 'r') as fh:
    configlines = fh.readlines()

# first line is the name of the destination zip file
dest_zip = configlines[0].strip("\n")
if dest_zip.lower().count('.zip') != 1:
    print("error: first line should be the name of the target zip file")
    sys.exit(1)

# fancy useful replacements in the filename
replace_map = {
    '{date}': datetime.today().strftime("%d-%m-%Y")
}
for original, replacement in replace_map.items():
    dest_zip = dest_zip.replace(original, replacement)

# 2nd line SHOULD be blank space
if configlines[1] != "\n":
    print("error: 2nd line should be blank")
    sys.exit(1)

# lines after that are source : target lines
dirmap_raw = configlines[2:]

dirmap = []
line_num = 1
for line in dirmap_raw:
    if line.count(':') != 1:
        print("error on line %i: mapping should be in the form of \"/source/folder : /target/folder/inside/zip\"" % line_num)
        sys.exit(1)

    source, target = line.split(':')
    source = source.strip()
    target = target.strip()

    if not source or not target:
        print("error on line %i: source or target folder missing" % line_num)
        sys.exit(1)

    dirmap.append((source, target))

    line_num += 1

prev_path = os.getcwd()
if not os.path.exists(TMPDIR):
    os.mkdir(TMPDIR)
os.chdir(TMPDIR)

for map in dirmap:
    source = map[0]
    target = map[1]

    print("copy %s => %s" % (source, target))

    shutil.copytree(source.rstrip('/'), target.rstrip('/'))

os.chdir(prev_path)

print("Compressing into %s.." % dest_zip)
shutil.make_archive(dest_zip, 'zip', TMPDIR)

shutil.rmtree(TMPDIR)