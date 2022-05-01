#Expected output
'''
confirm_ending("Bastian", "n") should return true.

confirm_ending("Congratulation", "on") should return true.

confirm_ending("Connor", "n") should return false.

confirm_ending("Walking on water and developing software from a specification are easy if both are frozen", "specification") should return false.

confirm_ending("He has to give me a new name", "name") should return true.

confirm_ending("Open sesame", "same") should return true.

confirm_ending("Open sesame", "sage") should return false.

confirm_ending("Open sesame", "game") should return false.

confirm_ending("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain") should return false.

confirm_ending("Abstraction", "action") should return true.
'''
def confirm_ending(string, target):
    '''
    confirm the ending
    '''
    flag = True
    for j in range(-1, -(len(target))-1, -1):
        if target[j] == string[j]:
            flag = True
        else:
            flag = False
            break
    if flag:
        return flag
    return flag


string = "asadfre hg"
target = "  g"
print(len(target))
print(confirm_ending(string, target))
