from functools import reduce
from operator import mul

def multiply_all(*numbers):

    # product = 1

    # for i in numbers:
    #     product *= i

    # return product


    return reduce(mul, [i for i in numbers])


print(multiply_all(1, 2, 3, 4))
