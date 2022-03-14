

##
###### Python dont support function overloading
##class Netzwerk:
##    def __init__(self, name):
##        self.name = name
##
##    def fun(self):
##        print(self.name, "One")
##
##    def fun(self):
##        print(self.name, "Two")
##
##
##n_obj = Netzwerk("kohli")
##n_obj.fun()
##
##var = "a"
##var = "b"
##print(var)

### Here only the second fun() will get executed 

############################################################
## Data Hiding / Access Specifier
## python has access specifier public, private
## Private access specifier can also be called as Data HIdin


##class Netzwerk:
##    def __init__(self, name):
##        self.name = name
##
##    def __new(self):   ## Private access can be defined by __
##        print(self.name, "Two")
##        
##    def fun(self):
##        print(self.name, "One")
##
##
##n_obj = Netzwerk("kohli")
##n_obj.fun()
####n_obj.new()




#############################################################

### Single Inheritance

#############################################################


##class Netzwerk:
##    def __init__(self, name):
##        self.name = name
##
##    def fun(self):
##        print(self.name, "One")
##
##class Two(Netzwerk):
##    def new(abhi):
##        print(abhi.name, "Two")
##
##n_obj = Two("Kohli")
##n_obj.fun()
##n_obj.new()


##class Netzwerk:
####    def __init__(self, name):
####        self.name = name
######        self.age = age
##
##    def fun(self):
##        print(self.name, "One")
##
##class Two(Netzwerk):
##    def __init__(abhi, name, age):
##        abhi.name = name
####        Netzwerk.__init__(abhi, abhi.name, 33)
##        
##    def new(abhi):
##        print(abhi.name, "Two")
##
##n_obj = Two("Kohli", 33)
##n_obj.fun()
##n_obj.new()
##
##
##num = 1
##def fun(num):
####    global num
##    print('num is: ',num)
##    num = 3
##    print('changed num to: ',num)
##fun(num)
##print('now 'num)
##


class A:
    def fun(self):
        print("a")
class B(A):
    def fun(self):
        print("b")
class C(A):
    def fun(self):
        print("c")
class D(B,C): ### Multiple Inheritance
    def funa(self):
        print("d")

d = D()
d.fun()


## Method Resolution Order
## It Will give priority to the near by search (during version 3.x version of python)
## During old version of python i.e., 2.x searcch would have gone thr deep search
