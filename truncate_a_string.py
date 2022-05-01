#expected output
'''
truncate_string("A-tisket a-tasket A green and yellow basket", 8) should return the string A-tisket....

truncate_string("Peter Piper picked a peck of pickled peppers", 11) should return the string Peter Piper....

truncate_string("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length) should return the string A-tisket a-tasket A green and yellow basket.

truncate_string("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length + 2) should return the string A-tisket a-tasket A green and yellow basket.

truncate_string("A-", 1) should return the string A....

truncate_string("Absolutely Longer", 2) should return the string Ab....


'''

def truncate_string(str, num):
    '''
    truncate string 
    '''
    str=str[0:num]
    str1=(str+"...")
    return str1

string="dbdsjkn dsnjks jsdnjksdnsk sdkndkn"
print(truncate_string(string,6))
