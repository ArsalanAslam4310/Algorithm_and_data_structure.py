#Expected Output
'''
find_longest_word_length("The quick brown fox jumped over the lazy dog") should return a number.

find_longest_word_length("The quick brown fox jumped over the lazy dog") should return 6.

ffind_longest_word_length("May the force be with you") should return 5.

find_longest_word_length("Google do a barrel roll") should return 6.

find_longest_word_length("What is the average airspeed velocity of an unladen swallow") should return 8.

find_longest_word_length("What if we try a super-long word such as otorhinolaryngology") should return 19.
'''
def find_longest_word_length(string):
    '''
    find large word lenght in string
    '''
    maximum = 0
    sub_stri_leng = 0
    j = 0

    for i in range(len(string)):
        j = i
        sub_stri_leng = 0

        while string[j] != " " and j < len(string)-1:
            j += 1
            sub_stri_leng += 1
            if sub_stri_leng > maximum:
                maximum = sub_stri_leng

    return maximum


stri = "dbxjh hdbxjhnb jasbxnxb xbzjhbsdjhxgujhdb dbxn"
print(find_longest_word_length(stri))
