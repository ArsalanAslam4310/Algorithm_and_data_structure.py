#expected output
'''
repeat_string_num_times("*", 3) should return the string ***.

repeat_string_num_times("abc", 3) should return the string abcabcabc.

repeat_string_num_times("abc", 4) should return the string abcabcabcabc.

repeat_string_num_times("abc", 1) should return the string abc.

repeat_string_num_times("*", 8) should return the string ********.

repeat_string_num_times("abc", -2) should return an empty string ("").

repeat_string_num_times("abc", 0) should return "".
'''
def repeated_repeat_string_num_times(string,num):
    '''
    string repeated
    '''
    repeat=string*num
    return repeat

string="sbd"
print(repeated_repeat_string_num_times(string,6))
