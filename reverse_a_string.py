def reverse(lis):
    new = []

    for i in range(len(lis)-1,-1,-1):
        new.append(lis[i])
    return new

li=[6,7,8,9,7,555,77]
print(reverse(li))
