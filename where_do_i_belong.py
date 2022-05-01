#Expected output
'''
get_index_to_ins([10, 20, 30, 40, 50], 35) should return 3.

get_index_to_ins([10, 20, 30, 40, 50], 35) should return a number.

get_index_to_ins([10, 20, 30, 40, 50], 30) should return 2.

get_index_to_ins([10, 20, 30, 40, 50], 30) should return a number.

get_index_to_ins([40, 60], 50) should return 1.

get_index_to_ins([40, 60], 50) should return a number.

get_index_to_ins([3, 10, 5], 3) should return 0.

get_index_to_ins([3, 10, 5], 3) should return a number.

get_index_to_ins([5, 3, 20, 3], 5) should return 2.

get_index_to_ins([5, 3, 20, 3], 5) should return a number.

get_index_to_ins([2, 20, 10], 19) should return 2.

get_index_to_ins([2, 20, 10], 19) should return a number.

get_index_to_ins([2, 5, 10], 15) should return 3.

get_index_to_ins([2, 5, 10], 15) should return a number.

get_index_to_ins([], 1) should return 0.

get_index_to_ins([], 1) should return a number.


'''

def get_index_to_ins(lis, num):
    '''
    Where do i belong
    '''
    sorted_copy = sorted(lis)
    i = 0
    while num >= sorted_copy[i]:
        i += 1
    return i


print(get_index_to_ins([0, 20, 30, 40, 50], 35))
