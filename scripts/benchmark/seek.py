#!/usr/bin/env python

import time
import random
import string
import tempfile
import os

filename="/data/bigbrain_40microns.nii"


old_offset = 0
f = open(filename,"r")
while(True):
    # Picks a random file size between 256 MB and 4718440448 (size of file)
    offset = random.randint(0,81523750352)
    small_distance = random.randint(-1024**3,1024**3)

    seek_start = time.time()
    f.seek(offset)
    seek_end = time.time()
    small_start = time.time()
    f.seek(offset+small_distance)
    small_end = time.time()  

   
    # Print result
    out = open("benchmark-seek-hdd-1.csv","a")
    out.write(''+str(offset-old_offset)+","+str(seek_end-seek_start)+"\n")
    out.write(''+str(small_distance)+","+str(small_end-small_start)+"\n")
    out.close()
    old_offset=offset
    # Just in case...
    time.sleep(1)
    
