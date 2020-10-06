# Your code here
import random
import math

#lookup tables are the same as dictionaries {}

"""
U

INPUT: two integers x and y
OUTPUT: integer that is the computation of all the math equations
the print statement is going to print 

P
- create a dictionary (cache)
- check if (x, y) is in cache
- if yes, return cache at index (x,y)
- else, set cache at index (x, y) = the_other_function(x, y)

E
R
"""
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if (x, y) in cache:
        return cache[(x, y)]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[(x, y)] = v
        return v



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
