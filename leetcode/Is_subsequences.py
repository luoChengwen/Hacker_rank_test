'''
Is Subsequence

Solution
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''


# solution 1
class Solution(object):
    def isSubsequence(self, s, t):

        while s and t:

            if s[0] == t[0]:
                s = s[1:]
                t = t[1:]
            else:
                t = t[1:]

        if len(s) == 0:
            return True
        else:
            return False

# solution 1
class Solution(object):
    def isSubsequence(self, s, t):

        if len(s) == 0: return True

        si, ti = 0, 0

        while si <= (len(s) - 1) and ti <= (len(t) - 1):

            if s[si] == t[ti]:
                si += 1
                if si == len(s):
                    return True
            ti += 1
        return False
