class Solution:
    def findMaxLength(self, nums) -> int:
        maxlen, sum_a = 0, 0
        hashmap = {0: -1}
        for i in range(len(nums)):
            sum_a = sum_a + 1 if nums[i] == 1 else sum_a - 1
            if sum_a not in hashmap:
                hashmap[sum_a] = i
            else:
                maxlen = max(maxlen, i - hashmap[sum_a])

        return maxlen


