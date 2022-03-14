import pandas

var = [4,5,2,3]
print(type(var))
print(var)

pd_var = pandas.Series(var)
print(type(pd_var))
print(pd_var)
sum_output = sum(pd_var)
print(sum_output)
