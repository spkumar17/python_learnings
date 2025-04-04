from array import *

arr = array("i",[])
n= int(input("enter the range "))

for i in range(n):
    arr.append(int(input("enter the values")))
print(arr)

var = int(input("enter the value you want to search"))

if var in arr:
    print(arr.index(var))
else:
    print(f"{var} is not in array.")
