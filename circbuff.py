
# This program is written for Python3
# Usage: python3 circbuff.py

# Program to read file in bytes, write the bytes to a buffer (in bytes), and write those bytes to a file

# specify input and output file names here
# The size of buffer is N
# The file should be less than the size of N or else the buffer will be overwritten.
# Also, the program kicks out if the file size is greater than N

# author: Prasad Golla
# March 2020

from array import array

N = 100
n = 0
cbhead = 0
cbtail = 0

IN_DIR="./"
OUT_DIR="./"
IN_FILE="inputfile.txt"
OUT_FILE="outputfile.txt"

circbuff = bytearray(N)

######################################################################
# read input file routine
# read until the end of file
# the size of file should be less than N or it will give an error
######################################################################
def readInputByByte():
    myfile = IN_DIR + IN_FILE;
    print("Opening input file: ", myfile)
   
    global cbtail
    global cbhead
    global circbuff

    try:
      with open(IN_FILE, "rb") as inf:
        filedata = array('B', inf.read())

      n = 0 # resetting n
      for byt in filedata:
        #print("byte read: ", byt)
        n = n + 1
        if (n == N):
           print("The file is bigger than the buffer size of: ", N)
           print("Quitting!")
           exit()
        circbuff[cbtail] = byt
        cbtail += 1
        if (cbtail == N):
            cbtail = 0
        #print("cbtail is: ", cbtail)
    except Exception as err:
        print("Error in readInputByByte with file: ", IN_FILE)
        print(err)

    print("Number of bytes read from file: ", n)

def writeBufferToFile():
    global cbtail
    global cbhead
    global circbuff
    try:
      myoutfile = OUT_DIR + OUT_FILE;
      print("Opening input file: ", myoutfile)
      with open(myoutfile, "wb") as outf:
          while(somethingInBuff()):
            i = cbhead
            x = circbuff[i:i+1]
            #print("writing: ", x)
            outf.write(x)
            cbhead += 1
            if (cbhead == N):
               cbhead = 0
            #print("i is: ", i)
    except Exception as err:
        print("Error in writeBufferToFile with file: ", OUT_FILE)
        print(err)

def somethingInBuff():
    global cbtail
    global cbhead
    if (cbhead == cbtail):
        return False
    else:
        return True

def bufferstat():
    global cbtail
    global cbhead
    global circbuff
    print("** Buff Stats **")
    print("buffer head is", cbhead)
    print("buffer tail is", cbtail)
    print("There are bytes in the buffer: ", somethingInBuff())
    print("Size of buffer: ", (cbtail - cbhead) if cbtail >= cbhead else (N + cbtail - cbhead) )
    print("****")

bufferstat()
readInputByByte()
bufferstat()
writeBufferToFile()
bufferstat()


