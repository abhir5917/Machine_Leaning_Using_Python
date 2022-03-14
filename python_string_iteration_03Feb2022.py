#### Iterator / loop

##var = "Abhijeet"
##for x in var:
##    print(x)

##
##var = "Abhijeet"
####for x in var:
####    print(x,end = "_")
##
##
##for x,y in enumerate(var):
##    print (x,y)

###Counting string length

##var = "My Name is ABhijeet"
##print(len(var))
##
##my_counter = 0
##for x in var:
##    my_counter += my_counter 
##print("length of", var, " = " , my_counter)


### conditional statement

##var = "I am Abhijeet. I live in Pune."
##for x in var:
##    if x == "i":
##        print(x, "Success")
##    elif x == "a":
##        print(x,"Success")
##    else:
##        print(x, "Failure")


### OR Statement

##for x in var:
##    if x =="i" or x == "a":
##        print(x,"Success")
##    else:
##        print(x,"Failure")
##

#### Break and continue
##var = "I am Abhijeet. I live in Pune."
##for x in var:
##    if x =="i" or x == "a":
##        print(x,"Success")
##        break
##    else:
##        print(x,"Failure")

##var = "I am Abhijeet. I live in Pune."
##for x in var:
##    if x == "i":
##        print(x,"Success")
##    continue



##var = "I am Abhijeet. I live in Pune."
##
##for x,y in enumerate(var):
##    if x == 4:
##        print(x, y, "Success")
##        break
##    else:
##        print(x,y, "Failure")

##var = "I am Abhijeet. I live in Pune."
##print("Input string= " +var)
##for x, y in enumerate(var):
##    if x %2 ==0:
##        print(x, y)


var = "I am Abhijeet. I live in Pune."
print("Input string= " +var)
odd_var = ""
even_var = ""
for x, y in enumerate(var):
    if x %2 ==0:
        even_var = even_var + y
    else:
        odd_var = odd_var + y
print("Odd Var = ",odd_var)
print("Even Var = ",even_var)
















