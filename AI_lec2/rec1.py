# how recursion loops through operations


def walk_rec(steps):
    if steps == 0:
        return
    walk_rec(steps - 1)
    print(f'made step #{steps}')



def walk_iter(steps):
    for i in range(1, steps + 1):
        print(f'made step #{i}')



print('walking iteratively')
walk_iter(3)
print('walking recursively')
walk_rec(3)