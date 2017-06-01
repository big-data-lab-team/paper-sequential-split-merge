#!/usr/bin/env python

import time
import random
import string
import tempfile
import os

# A 256 MB random string
print "Creating random string of 256MB..."
s= ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(256*1024*1024))
    
while(True):
    # Picks a random file size between 256 MB and 6 GB.
    # size is expressed in multiples of 256MB
    size = random.randint(1,24)
    
    # Generates the string we will write to disk
    buff = ''
    n = 0
    while ( n < size ):
        buff += s
        n += 1

    # Creates temp file and writes buffer
    fd, filename = tempfile.mkstemp(dir=os.getcwd())
    f = open(filename,"w")
    write_start = time.time()
    f.write(buff)
    write_end = time.time()
    f.close()
    f = open(filename,"r")
    read_start = time.time()
    f.read(len(buff))
    read_end = time.time()
    f.close()
    os.remove(filename)
    
    # Print result
    print len(buff),filename,write_end-write_start,read_end-read_start
    # Just in case...
    time.sleep(1)
    
