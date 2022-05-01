#Expected Output
'''
find_longest_word_length("The quick brown fox jumped over the lazy dog") should return a number.

find_longest_word_length("The quick brown fox jumped over the lazy dog") should return 6.

ffind_longest_word_length("May the force be with you") should return 5.

find_longest_word_length("Google do a barrel roll") should return 6.

find_longest_word_length("What is the average airspeed velocity of an unladen swallow") should return 8.

find_longest_word_length("What if we try a super-long word such as otorhinolaryngology") should return 19.
'''
def find_longest_word_length(lis):
    '''
    find longest word in string
    '''
    maximum = len(lis)

    for word in lis:
        if len(word)>maximum:
            maximum= len(word)
    return maximum

li=["dbxjh","hdbxjhnb","jasbxnxb","xbzjhbsdjhxgujhdb","dbxn"]
print(find_longest_word_length(li))
