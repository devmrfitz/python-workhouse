#Default template for python in competitive programming

#template begins
##############################################################
# import libraries for input/ output handling
# on generic level
import atexit, io, sys
 
# A stream implementation using an in-memory bytes 
# buffer. It inherits BufferedIOBase.
buffer = io.BytesIO()
sys.stdout = buffer
 
# print via here
@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())

import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#Use: a,b,c,d = get_ints()
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
#Use: Arr = get_list()

##############################################################
#template ends
