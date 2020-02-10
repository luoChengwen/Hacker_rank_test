# find out anagram in a string

'''
# 'accca'
[0,4] , a - a , 1st pair
[1,2] , [1,3] ,[2,3],   c-c, 2nd, 3rd and 4th pair
[0:2 ,3:5] ac - ca 5th pair
cc, cc 6th pair
acc - cca 7th pair
accc - ccca 8th

'''

import collections


def ana_gram(s):
    sub_string = []
    num = 0
    for length in range(1,len(s) - 1 + 1):  # length of string, from 1 to len(s) - 1:
        for j in range(0,len(s) - length + 1):
            sub_string.append(s[j:j+length])

    sub_string = [''.join(sorted(i)) for i in sub_string]
    counter = collections.Counter(sub_string)

    for n in counter:
        num += counter[n] * (counter[n] - 1)/2
    return int(num)
