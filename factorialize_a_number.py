# Expected output:

'''
factorialize(5) should return a number.

factorialize(5) should return 120.

factorialize(10) should return 3628800.

factorialize(20) should return 2432902008176640000.

factorialize(0) should return 1.


'''
def factorialize(value):
    '''
    factor of number
    '''
    fact = value
    for i in range(1,fact):
        fact = fact*i
    return fact


print(factorialize(5))
