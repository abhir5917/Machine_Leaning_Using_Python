###### Exception

### Every Exception belongs to parent class Exception

##try:
##    var = 10/0
##except TypeError:
##    print("Sorry")
##except Exception as ex:
##    print(ex)
##
##print("Welcome")


## Every try must have at least 1 except block


### try...except...else

### try should contains the statement which may give you error
### except will execute if any exception is occurredin statements under try
## else will get execute if there is no exception in try statements
## finally will gets executed irrespective of exception occuring in try block
## finally should be the last block
## Sequence should always be try..except...else...finally
## finlly mainly used in db related codes to close the connections to db
##
##try:
##    var = 10/0
##except Exception as ex:
##    print(ex)
##else:
##    print("No Exception")
##finally:
##    print("This is finally always gets prited")


##############################################################################################################################
##############################################################################################################################

### Raise::: It is used to raise an exception in case of any particular condition is met

##try:
##    for i in range(10):
##    
##        if i>5:
##            raise IndexError            ### Here in this loop if value of i becomes 5 it will raise an IndexError
##        print(i)
##except IndexError:
##    print("ghghghgh4")

### USer Defined Exception

class MyError(Exception):
    var = "my own error"
try:
    var = 10
    if var> 5:
        raise MyError
except MyError as Ex:
    print(Ex)
    
