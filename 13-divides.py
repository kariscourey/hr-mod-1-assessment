def divides_evenly(numerator, denominator):
    if denominator == 0:
        return False
    return (numerator % denominator) == False



print(divides_evenly(6,1.5))
print(divides_evenly(6,2))
print(divides_evenly(6,3))
print(divides_evenly(6,4))
print(divides_evenly(0,4))
print(divides_evenly(6,0))
