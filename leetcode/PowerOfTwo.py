'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''

#solution 1: intuitive

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        i = 0

        while True:
            num = 2 ** i
            if num == n:
                return True
            elif num > n:
                return False
            i += 1

# solutio 2
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0: return False

        while n != 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True

