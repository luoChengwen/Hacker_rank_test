'''
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
'''
# intuitive but slow, solution 2,3 passed all tests
class Solution:
    def maxSubarraySumCircular(self, A) -> int:
        if len(A) == 1:
            return A[0]

        Nlen = len(A)
        A2 = A * 2
        maxSum = A[0]

        def maxsumfunc(arr):
            max_end_here = 0
            arr_max_sum = arr[0]

            for num in range(len(arr)):
                max_end_here += arr[num]
                if max_end_here < arr[num]:
                    max_end_here = arr[num]
                arr_max_sum = max(arr_max_sum, max_end_here)
            return arr_max_sum

        for i in range(len(A2) - Nlen):
            temp_arr = A2[i: (i + Nlen)]
            temp_max = maxsumfunc(temp_arr)
            maxSum = max(temp_max, maxSum)

        return maxSum


# solution 2
class Solution:
    def maxSubarraySumCircular(self, A) -> int:

        def maxsumfunc(arr):
            max_end_here = 0
            arr_max_sum = arr[0]

            for num in range(len(arr)):
                max_end_here = max(max_end_here + arr[num], arr[num])
                arr_max_sum = max(arr_max_sum, max_end_here)
            return arr_max_sum

        maxSum_A = maxsumfunc(A)
        max_wrap = sum(A)
        A2 = [-i for i in A]
        maxSum_B = maxsumfunc(A2)
        maxSum_B += max_wrap
        return max(maxSum_A, maxSum_B) if maxSum_A > 0 else maxSum_A

# solution 3
class Solution:
    def maxSubarraySumCircular(self, A):
        curMax, maxSum, curMin, minSum = 0, -float('inf'), 0, float('inf')
        total = 0

        # now goes through A, updating these
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(curMin, minSum)
            total += a

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


