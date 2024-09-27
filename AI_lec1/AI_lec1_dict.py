# dict examples

import random

d1 = {'irakli':31, 'sandro':24, 'ani':29}
d1['lika'] = 30
print(d1)
print(d1.keys(), d1.values(), d1.items())

# random list with 10000 numbers 0-9
random_list = []
for i in range(10000):
    random_list.append(random.randrange(0,10))
print(random_list[-25:])

# find out how much numbers we have
number_count = {}
for elem in random_list:
    if elem in number_count.keys():
        number_count[elem] += 1
    else:
        number_count[elem] = 1
        
print(number_count)
print(sum(number_count.values()))
