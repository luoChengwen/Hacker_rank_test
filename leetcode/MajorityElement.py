'''
Majority Element
Solution
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''
# solution 1, using package.
from collections import Counter


class Solution:
    def majorityElement(self, nums) -> int:
        c = Counter(nums)
        majE = sorted(c.values())[-1]
        for i in c:
            if c[i] == majE:
                return i


# solution 2 will be similar, just build the dictionary as the imported package