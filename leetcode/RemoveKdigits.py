'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

# solution 1
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if k >= len(num): return '0'

        stack = []

        for i in num:
            stack.append(i)

            while len(stack) >= 2 and stack[-2] > stack[-1] and k > 0:
                stack.pop(-2)
                k -= 1

            while len(stack) >= 3 and stack[-2] > stack[-1] and stack[-2] > stack [-1] and k > 0:
                stack.pop(-2)
                k -= 1

        while k > 0:
            stack.pop()
            k -= 1

        while stack and stack[0] == '0':
            stack.pop(0)

        return ''.join(stack) if stack else '0'


# solution 2: a faster solution
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if k >= len(num): return '0'

        stack = []
        for i in num:
            while stack and k > 0 and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)

        while stack and stack[0] == '0':
            stack.pop(0)

        stack = stack[:(len(stack)-k)]

        return ''.join(stack) if stack else '0'





