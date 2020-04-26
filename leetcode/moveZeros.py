
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


'''
approach 1,
'''


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nozero, total_length = 0, 0
        for item in nums:
            if item != 0:
                nums[nozero] = item
                nozero += 1
            total_length +=1

        while nozero < total_length:
            nums[nozero] = 0
            nozero +=1

        return nums


'''
approach 2 , slower
'''


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        while i <= len(nums) - 2:
            j = i+1
            if nums[i] == 0:
                while nums[j] == 0 and j <= len(nums) - 2:
                    j += 1

                if j <= len(nums) - 1 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1

