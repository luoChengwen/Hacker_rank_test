
"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

## solution 1: intuitive


class Solution:
    def maxSubArray(self, nums) -> int:
        maxsum = nums[0]
        print(maxsum)
        start_pos = 0
        for i in range(len(nums)):
            single_sum = 0
            for j in range(start_pos, i + 1):
                single_sum += nums[j]
                print(nums[j],single_sum )
            maxsum = max(maxsum, single_sum)
            if single_sum < 0:
                start_pos = j + 1
                single_sum = 0

            print(single_sum, maxsum)

        return maxsum


# solution 2: dynamic programming https://www.youtube.com/watch?v=2MmGzdiKR9Y
