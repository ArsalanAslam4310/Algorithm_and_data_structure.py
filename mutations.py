#expected output
'''
mutation(["hello", "hey"]) should return false.

mutation(["hello", "Hello"]) should return true.

mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]) should return true.

mutation(["Mary", "Army"]) should return true.

mutation(["Mary", "Aarmy"]) should return true.

mutation(["Alien", "line"]) should return true.

mutation(["floor", "for"]) should return true.

mutation(["hello", "neo"]) should return false.

mutation(["voodoo", "no"]) should return false.

mutation(["ate", "date"]) should return false.

mutation(["Tiger", "Zebra"]) should return false.

mutation(["Noel", "Ole"]) should return true.


'''

def mutation(lis,target):
    '''
    mutation of string
    '''
    
    for i in range(len(lis)):
        if lis[i]== target:
            return True
        else:
            return False

stri=["hello"]
print(mutation(stri,"hello"))
