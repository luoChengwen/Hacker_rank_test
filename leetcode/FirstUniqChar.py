'''
First Unique Character in a String
Solution
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


# intuitive, use dictionary
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_set = set(s)
        set_c = dict()

        for i in s_set:
            set_c[i] = s.count(i)

        uniques = [uniqu for uniqu in set_c if s.count(uniqu)==1]

        for i in range(len(s)):
            if s[i] in uniques:
                return i

        return -1


# solution 2:
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1