#### File Operations

#### There are 3 major parts in a file operations-
# 1) open file
# 2) write in file
# 3) close the file

##file_obj = open("abc.txt", 'w')  ## // opens a file in write mode, creates file if the file is not present
##file_obj.write("hello") ## Write in the file
##file_obj.close()   ## Close the file

import tkinter ##GUI, Forms, frames, buttons, labels
from tkinter import filedialog
import os

##root = tkinter.Tk()
##root.withdraw()
##
##folder = filedialog.askdirectory()
##print(folder)
##
##file = os.path.join(folder, "abc.txt")
##
##file_obj = open(file,"a")
##file_obj.write(" is my country")
##file_obj.close()


### Context Manager
## with statement in python are used as context manager

##with open("abc.txt", "w") as file_obj:
##    file_obj.write("this is")

##Python Read Operations
# Open the file in read mode using r operation

# 1) read() used to read all contents from file
# 2) read(10) reads 10 characters from file.
# 3) after read(n) if you again read the file which is already open , it will start reading n characteer onwards only
# 4) readline() will read a line from file, after once readline if we again readline() will read next line

##with open("abc.txt" , "r") as file_obj:   ### Opens file in read mode stores in file_obj for referring
##    file_content = file_obj.read()  ### Reads entire file abc.txt and stores content in file_content
##    print(file_content)    ### Prints file_content on screen
##    

##with open("abc.txt" , "r") as file_obj:   ### Opens file in read mode stores in file_obj for referring
##    file_content = file_obj.read(10)  ### Reads first 10 characters from file abc.txt and stores content in file_content anfter reading the cursor will stay after 10th char
##    print(file_content)    ### Prints file_content on screen
##    file_content1 = file_obj.read()  ## Reads entire file but as cursor in file_obj is at 11th char, will start reading from 11th char and store content in file_content1
##    print(file_content1)
##
##with open("abc.txt" , "r") as file_obj:   ### Opens file in read mode stores in file_obj for referring
##    file_content = file_obj.readline()  ### Reads first linefrom file abc.txt and stores content in file_content after reading the cursor will stay onsecond line
##    print(file_content)    ### Prints file_content on screen
##    file_content1 = file_obj.readline()  ## Reads one line from file but as cursor in file_obj is at snd line, will read2nd line only and store content in file_content1
##    print(file_content1)

##with open("abc.txt" , "r") as file_obj:   ### Opens file in read mode stores in file_obj for referring
##    file_content = file_obj.readlines()  ### Reads and stores all lines from the file and store in list
##    print(file_content) ### Prints file_content on screen
##    print(type(file_content))

############################################################################
## Python Read/Write operation
## Use w+ inoperator while opening the file e.g open("abc.txt", w+)
## Same we have a+ operator, it will allow to write and read but contents wont override
## we have r+ as well, which will open file in read plus append mode
## seek(n) method used to reset the cursor position to nth position

with open("abc5.txt", "x+") as f_obj:
##    f_obj.seek(0)
##    file_content = f_obj.read()
    f_obj.write("\nNew Line added")
    f_obj.seek(0)
    f_obj.write("\nNew Line added2")
    f_obj.seek(0)
    file_content = f_obj.read()
    print(file_content)   
##    print(file_content)


## there is also one more operator x available, that will open file in write mode only plus append mode, provided the file will always get created, you cant do this on previously created file
