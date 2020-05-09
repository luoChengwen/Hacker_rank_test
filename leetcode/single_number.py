
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''



class Solution:
    def singleNumber(self, nums): #nums is a list
        ans = nums[0]
        for i in range(1, len(nums)):
            print(ans, nums[i])
            ans ^= nums[i]   # the idea of xor
            print(ans)
        return ans


# solution 2, easier to understand
from collections import Counter
class Solution:

    def singleNumber(self, nums):
        all_val = Counter(nums)
        for i in all_val:
            if all_val[i] == 1:

                return i