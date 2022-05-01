#expected output
'''
chunk_array_in_groups(["a", "b", "c", "d"], 2) should return [["a", "b"], ["c", "d"]].

chunk_array_in_groups([0, 1, 2, 3, 4, 5], 3) should return [[0, 1, 2], [3, 4, 5]].

chunk_array_in_groups([0, 1, 2, 3, 4, 5], 2) should return [[0, 1], [2, 3], [4, 5]].

chunk_array_in_groups([0, 1, 2, 3, 4, 5], 4) should return [[0, 1, 2, 3], [4, 5]].

chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6], 3) should return [[0, 1, 2], [3, 4, 5], [6]].

chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4) should return [[0, 1, 2, 3], [4, 5, 6, 7], [8]].

chunk_array_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2) should return [[0, 1], [2, 3], [4, 5], [6, 7], [8]].
'''

def chunk_array_in_groups(lis,size):
    '''
    convert a list to lists
    '''
    inner_list=[]
    outer_list=[]

    idx=0
    for _ in range(size):
        i=0
        while i<len(lis)//size:
            inner_list.append(lis[idx])
            idx+=1
            i+=1
        outer_list.append(inner_list)
        inner_list=[]
    return outer_list

lis=[6,6,54,3,22,2]
print(chunk_array_in_groups(lis,3))
