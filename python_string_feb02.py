##var = "dhoni msd"
##print(var)
##print([var[0]])
##slicing
## var[start:end] string slicing from start to end, in if kept blank will print complete
##print(var[0:])   ## Start is 0 end not specief, will strat from 0 till end
##print(var[2:6])  ## Start from 2nd till 6th
##print(var[-1])   ## only one letter at location -1 i.e last char
##print(var[-1:-2])  
##print(var[::]) ##No start end specified

## string ops
##print(var[::-1]) ##STring reversal
## var[start:end:step]
##print(var[::2])  ## Print complete string with step value as 2, skips one letter
##print(var[::-2]) ##takes step 2 but start from -1
##var, var1 = "dhoni", "msd"
##print(var)
##print(var1)


####concating string
##
##name = "dhoni"
##score = 183
####statement = "captain scored against Srilanka" #insering dhoni and 183 in between statement#
##
####statement = "captain" + name + "scored" + str(score) + "againts srilanka"
##
####statement = "captain %s scored %d against srilanka"%(name,score)
### Above statement works if we know type of name and score variables
#### When we dont know type we can use below
##
####statement= "captain {} scored {} against srilanka".format(name, score)
##statement = f"captain {name} scored {score} against srilanka"
##print(statement)

#### Multiline string declaration

##var = """ My name is Abhijeet 
##I am from Pune"""


##var = """ My name is Abhijeet \
##I am from Pune"""

##var = " My name is Abhijeet \
##I am from Pune"
##
##print(var)
##


#### Raw strings

##path = "c:\new Folder\test.txt"  ## In this line \n will be consider as new line escape character
## TO avoid use r while declaring string as below
path = r"c:\new Folder\test.txt"
print(path)













