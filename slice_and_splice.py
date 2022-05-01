#Expected output
'''
franken_splice([1, 2, 3], [4, 5], 1) should return [4, 1, 2, 3, 5].

franken_splice([1, 2], ["a", "b"], 1) should return ["a", 1, 2, "b"].

franken_splice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2) should return ["head", "shoulders", "claw", "tentacle", "knees", "toes"].


'''

def franken_splice(arr1, arr2, n):
    '''
    put the value at n index
    '''
    i = n
    j = 0
    while j < len(arr1):
        arr2.insert(i, arr1[j])
        j += 1
        i += 1
    return arr2


li = [1, 2, 3]
li1 = [4, 5, 7, 6]
print(franken_splice(li, li1, 0))
