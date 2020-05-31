'''
Counting Bits: ###this one is difficult!!!
Solution
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = [0]
        for i in range(1, num + 1):
            output.append(output[i >> 1] + int(i & 1))
            # int here is import or at least put a () ..... for instance:
            # 3>>1 + 3 >>1 = 0
            # but, int(3>>1) + int(3>>1) = 2 or (3>>1) + (3>>1) = 2

        return output

