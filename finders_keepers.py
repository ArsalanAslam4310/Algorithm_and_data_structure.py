#Expected output
'''
find_element([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; }) should return 8.

find_element([1, 3, 5, 9], function(num) { return num % 2 === 0; }) should return undefined.
'''
def find_element(lis, func):
    '''
    Find element in list
    '''
    for val in lis:
        if func(val):
            return val
    return None


li = [1, 3, 5, 9, 8]
print(find_element(li, lambda x: x % 2 == 0))
