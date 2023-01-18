import numpy as np

def find_num(x):
    ar = np.random.randint(1, 100, 100)
    d = 0
    found = False
    print(ar)
    for i in ar:
        d+=1
        if d<len(ar):
            if x == i:
                print(f'{x} is present at {d} position')
                found = True
        else:
            if found == False:
                print(f'{x} not found.')

find_num(int(input('Enter the numberr to find : ')))