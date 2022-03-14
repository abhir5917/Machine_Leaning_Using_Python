##********************Functions********************##

##def fun():
##
##    print("hello")
##    print("welcome to hdfc")
##
##fun()
##fun()


##def fun(var):
##    print("hello", var)
##    print("welcome to hdfc")
##
##fun("kohli")
##fun("dhoni")
##fun(5)

##
##def fun(var):
##    if isinstance(var, str):
##        print("hello", var)
##        print("welcome to hdfc")
##
##fun("kohli")
##fun("dhoni")
##fun(5)

########
##isinstance(variable, type):: The isinstance method is a method that checks if
##the variable that is passed to the method, is of type specified in type, if so
##returns true else false.
########



##def fun(var, country):
##    if isinstance(var, str):
##        if isinstance(country, str):
##            print("hello", var, "from", country)
##            print("welcome to hdfc")
##
##fun("kohli", "india")
##fun("dhoni", "aus")
##fun("rohit", 5)


##def fun(var, country):
##    if isinstance(var, str)and isinstance(country, str):
##            print("hello", var, "from", country)
##            print("welcome to hdfc")
##
##fun("kohli", "india")
##fun("dhoni", "aus")
##fun("rohit", 5)


###### function with keyword...
##def fun(var, country):
##    if isinstance(var, str)and isinstance(country, str):
##            print("hello", var, "from", country)
##            print("welcome to hdfc")
##
##fun(country = "india",var = "kohli" ) ### here as defined with keyword the sequence of argument will not matter as var will contain kohli even if passed at 2nd position.
##fun("dhoni", "aus") ### Here dhoni will assigned to var and aus as country
##fun("rohit", 5)


#### Function with default argument
##
##def fun(var="India", country):
##    if isinstance(var, str)and isinstance(country, str):
##            print("hello", var, "from", country)
##            print("welcome to hdfc")
##
##fun(country = "india",var = "kohli" ) ### here as defined with keyword the sequence of argument will not matter as var will contain kohli even if passed at 2nd position.
##fun("dhoni", "aus") ### Here dhoni will assigned to var and aus as country
##fun("rohit")
##
##Output:
##    Non default argument follows default argument in defination


##def fun(var, country= "India"):
##    if isinstance(var, str)and isinstance(country, str):
##            print("hello", var, "from", country)
##            print("welcome to hdfc")
##
##fun(country = "india",var = "kohli" ) ### here as defined with keyword the sequence of argument will not matter as var will contain kohli even if passed at 2nd position.
##fun("dhoni", "Aus") 
##fun("rohit") ## Here only 1 arg passed, it will by default keep country as india, as specified in the function defination
##


####################### *args
##
##def passed_students(*name): ## *args   -  arguments
##    print(name)
##    print(type(name))
##
##passed_students("dhoni","kohli")

#### when *args passed in function defination as an argument, it can take any number of aruguments while calling
##and the function will get called that many times the arguments are passed
## the type of *args variable will be tuple


################ **KWARGS
##def passed_students(**name):  ## *kwargs   - keyword arguments
##    print(name)
##    print(type(name))
##
##passed_students(name = "dhoni",Age = 33)
##passed_students(name = "dhoni",Team = "kohli")

## Output:
##('dhoni', 'kohli')
##<class 'tuple'>
##{'name': 'dhoni', 'Age': 33}
##<class 'dict'>
##{'name': 'dhoni', 'Team': 'kohli'}
##<class 'dict'>


## **kwargs -- keyword arguments
## while defining give the arg name with **
## accepts arguments in form of dictionaries

###v return statemsnt

#when a fuction returs something use return in defination

def student_marks(name, eng, maths):
    total = eng+maths
    return total, name
total = student_marks("dhoni", 44, 55)
print(total)
