#expected_output
'''
title_case("I'm a little tea pot") should return a string.

title_case("I'm a little tea pot") should return the string I'm A Little Tea Pot.

title_case("sHoRt AnD sToUt") should return the string Short And Stout.

title_case("HERE IS MY HANDLE HERE IS MY SPOUT") should return the string Here Is My Handle Here Is My Spout.


'''


def title_case(string):
    '''
    convert a string to title case
    '''
    string = list(string.lower())
    string[0] = string[0].upper()
    for i in range(len(string)):
        if string[i] == " ":
            string[i+1] = string[i+1].upper()

    return "".join(string)


string = "I'm a little tea pot"
print(title_case(string))
