name = "prasanna Kumar"

print(name[0])
print(name[-1])
print(name[3: ])
print(name[ ::-1])
print(name[ -4::-1])
print(name[ -4:-1])

# len count the elements in the string
print(len(name))

string = "abcdefghijklmnopq"
print(string[0:4:2])
 
print(name.replace("a", "A"))  # Replaces all occurrences of "a" with "A"


#normally we can't modify the value in the string as below 
# name = 'sam'
#name[0] ='p'
# 
#but we can achieve this by concatinating the string 

name1 ='sam'
last_name =name1[1: ]
new_name ="P" + last_name
print(new_name)

print(new_name.upper())

print(new_name.lower())

print(name.split("a")) # ===this will split the string based in letter "a"---> ['pr', 's', 'nn', ' Kum', 'r']

# Using the format() method to insert values into the string
print( "my name is {}.I am a {}.".format("Prasanna kumar " , 'DevOps Engineer ' ))


# this will join the list of strings into a single string 

my_list = ['Hello', 'world']
print(" ".join(my_list))  # Outputs: "Hello world"
