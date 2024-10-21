# list comprehention template [expression for value in iterable if condition]

l1 = [2,7,13,9,5,10,7,12]

squares1 = []

# with loop
for i in l1:
    squares1.append(i*i)
print(squares1)

# with comprehention

squares2 = [i*i for i in l1]
print(squares2)

#squares3 = [i**2 for i in l1 if i % 2 == 0]
squares3 = [i**2 if i % 2 == 0 else i * 5 for i in l1]
print(squares3)

# list of lists
grid = [['-' for i in range(0,10)] for j in range(0,10)]
print(grid)

