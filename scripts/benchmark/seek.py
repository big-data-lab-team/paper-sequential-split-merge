#!/usr/bin/env python

import time
import random
import string
import tempfile
import os

filename="file.dat"


old_offset = 0
while(True):
    # Picks a random file size between 256 MB and 4718440448 (size of file)
    offset = random.randint(0,22548578304)

    f = open(filename,"w")
    seek_start = time.time()
    f.seek(offset)
    seek_end = time.time()
    f.close()
       
    # Print result
    out = open("benchmark-seek.csv","a")
    out.write(''+str(offset-old_offset)+","+str(seek_end-seek_start)+"\n")
    out.close()
    old_offset=offset
    # Just in case...
    time.sleep(1)
    
