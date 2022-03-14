## Dictionary
## Python Dictionary is a key value pair datatype
# No Index based manipulation
# Keys should be unique
# Declared inside curley braces {key1:value1, key2:value2,....}

##var = {}
##print(type(var))

# Incase used the key repeatedly will only give reslut of last repeated key's value
# The value at repeated key will be overriden

##var = {"name" : "Rohit", "Age" : 32, "name" : "Dhoni"}
##print(var)
### O/P : {'name': 'Dhoni', 'Age': 32}

##### No Index Based Manipulation
##var = {"name" : "Rohit", "Age" : 32, "name" : "Dhoni"}
##print(var[0])
##Traceback (most recent call last):
##  File "C:/Users/Amit/Desktop/Python/python_dictionary_08Feb2022.py", line 18, in <module>
##    print(var[0])
##KeyError: 0

# Dictionary is mutable, i.e we can change contains
##var = {"name" : "Dhoni", "Age" : 33, "Country" : "India"}
##print(f"Original Dictonary: {var}") var["name"] = "Kohle"
##print(f"Changed Dictonary: {var}")
##
#### Output:
##Original Dictonary: {'name': 'Dhoni', 'Age': 33, 'Country': 'India'}
##Changed Dictonary: {'name': 'Kohle', 'Age': 33, 'Country': 'India'}

##var = {"name" : "Dhoni", "Age" : 33, "Country" : "India"}
### whEN referred to the key that is not present will throw keyerror 
##output = var["team"]
##print(output)
## Output
##    output = var["team"]
##KeyError: 'team'

##var = {"name" : "Dhoni", "Age" : 33, "Country" : "India"}
##output = var.get("name","sorry")
##print(output)
##print("Welcome to INdia")
#### Output:
## sorry
## Welcome to INdia

##var = {"name" : "Dhoni", "Age" : 33, "Country" : "India"}
##output = var.get("name","sorry")
##print(output)
##print("Welcome to INdia")
###O/p
##Dhoni


##Welcome to INdia

##var = {"name":"Dhoni"}
##var1 = {"Age": 33}
##res = var + var1
##print(res)
##
##OP: Unsupported operands for + dict, dict


##my_list = []
##for x in range(10):
##    if x%2 == 0:
##        my_list.append(x)
##print (my_list)
#### ANother way of doing above in a single line
##my_list = [x for x in range(10) if x%2 == 0]
##print(my_list)


my_dict = {}
for x in range(4):
    my_dict[x] = x*x
print(my_dict)

my_dict = {x:x*x for x in range(4)}
print(my_dict)
