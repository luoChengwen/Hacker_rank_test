'''
Permutation in anagram
https://leetcode.com/problems/permutation-in-string/
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''
# solution 1:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def build_dict(compstr):
            compdict = dict()
            for m in compstr:
                if m in compdict: compdict[m] += 1
                else: compdict[m] = 1
            return compdict

        plen = len(s1)
        dict_p = build_dict(s1)
        for i in range(len(s2) - plen + 1):
            compstr = s2[i: (i + plen)]

            if i == 0: com_dict = build_dict(compstr)
            else:
                prev = s2[i - 1]
                com_dict[prev] -= 1
                if com_dict[prev] == 0: com_dict.pop(prev, None)
                new = s2[i + plen - 1]

                if new in com_dict: com_dict[new] += 1
                else: com_dict[new] = 1

            if com_dict == dict_p: return True

        return False
