#### Class is template
##class is going to have everything needed for the program to execute
##class in general is called as collection of objects

## Vehivle --
## Class is to form a structure


##Class Example:

##class Netzwerk:
##
##    var = "dhoni"
##    def fun():
##        print("Welcome")
##
##print(Netzwerk.var)
##Netzwerk.fun()


## Class and objects:
##class Netzwerk:
##
##    var = "dhoni"
##    def fun():
##        print("Welcome")
##
##n_obj = Netzwerk   ## Creating object of the class
##print(n_obj.var)
##n_obj.fun()
##print(n_obj)
##

#### OUtput
##dhoni
##Welcome
##<class '__main.Netzwerk'>

## Class with COnstructor

##class Netzwerk:
##
##    var = "dhoni"
##    def fun(abc):
##        print("Welcome", abc.var)
##
##n_obj = Netzwerk()   ## Creating object of the class calling a constructor
##print(n_obj.var)
##n_obj.fun()
##print(n_obj)


## Constructor calling
##
##class Netzwerk:
##
##    def __init__(self, name):   ## init method is called automatically whenevr object of class is created
##        self.name = name
##
##    def fun(self):
##        print("Welcome", self.name)
##
##    def new(self):
##        print(self.name," joined us")
##
##n_obj = Netzwerk("Abhijeet")
##n_obj.fun()
##n_obj.new()



########################################################################################################
##
class My_Class:
    """ This  is class defined with functions that takes argumment"""

    def __init__(self, name, age):
## Anything that has double underscore on either side is called "attributes" "magic methods"
## Self is called object reference for inside class
        self.name = name
        self.age =age

    def one(self):
        print(self.name)

    def two(self):
        print(self.age, self. name)

my = My_Class("dhoni", 33)
## my is called single object instance reference for outside activity
## My_Class() is called constructor
## By Default all the constructor will have one hidden argument in the first postition

my.one()
my.two()
print(my.__doc__)
