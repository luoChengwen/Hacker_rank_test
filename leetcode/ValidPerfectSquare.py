'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

# solution 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # two pointer

        if num <=1: return True

        left = 0
        right = num

        while True:

            if right ** 2 > num and left != right:
                mid = (left + right) // 2

                if left >= right or right - left == 1:
                    return False

                if mid ** 2 > num:
                    right = mid

                elif mid ** 2 == num:
                    return True

                else:
                    left = (left + right) // 2

        return False


# revisited the question by chance and new solution

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        start = num // 2
        s = False
        while True:
            if start ** 2 > num:
                start //= 2
                if s: return False
            elif start ** 2 < num:
                start += 1
                s = True
            else:
                return True


