# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
     
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n-2):
            target = nums[i] * -1
                            
            if nums[i] == nums[i-1] and i > 0: 
                continue
            
            s = i+1
            e = n-1
            
            while s< e:      
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s += 1
                    
                    while  s < e and nums[s] == nums[s-1]:
                        s += 1
                    
                elif nums[s] + nums[e] < target:
                    s+= 1
                
                else: e-=1
            
        return result
