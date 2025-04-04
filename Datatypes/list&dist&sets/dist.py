my_dist = {'k1': 100, 'k2': 200, 'k3': 300}

print(my_dist)

print(my_dist['k1'])

dist1 = {'k1':[1,2,3], 'k2': {'k21' :"string"}, 'k3': 300}

print(dist1['k2']['k21'])

print(dist1.keys())
print(dist1.values())

my_dist['k4'] = 400  # Adding a new key-value pair
my_dist['k1'] = 150  # Updating an existing value
del my_dist['k2']  # Removes the key 'k2'


print(my_dist)
print('k2' in my_dist)  # Outputs: True or False



