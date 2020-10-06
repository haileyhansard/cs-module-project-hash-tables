# Your code here

"""
U
if x <= 0, then return y + z
else if x > 0, return exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

Hint: In Python, a dict key can be any immutable type... including a
tuple.

Need to use the cache dictionary to make this go faster.
The key will be the tuple (x, y, z)?

P
E
R
"""

cache = {}

def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    # elif x > 0:
    #     cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    #     return cache[(x, y, z)]
    elif x > 0:
        try:
            return cache[(x, y, z)]
        except:
            cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
            return cache[(x, y, z)]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
