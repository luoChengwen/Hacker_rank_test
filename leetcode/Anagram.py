'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''


# solution 1: there are better ways
class Solution:
    def findAnagrams(self, s: str, p: str):
        def build_dict(compstr):
            compdict = dict()
            for m in compstr:
                if m in compdict:
                    compdict[m] += 1
                else:
                    compdict[m] = 1
            return compdict

        plen = len(p)
        dict_p = build_dict(p)
        to_disp = []
        for i in range(len(s) - plen + 1):
            compstr = s[i: (i + plen)]
            print(s)
            if i == 0:  # build dict for the first time
                com_dict = build_dict(compstr)
                print(com_dict)
            else:
                print(i)
                print(s[i])

                prev = s[i - 1]
                com_dict[prev] -= 1
                if com_dict[prev] == 0:
                    com_dict.pop(prev, None)

                new = s[i + plen - 1]
                print(new)
                print(new in com_dict, new, com_dict)



                if new in com_dict:
                    com_dict[new] += 1
                else:
                    com_dict[new] = 1
            print('---')

            if com_dict == dict_p:
                to_disp.append(i)

        return to_disp
