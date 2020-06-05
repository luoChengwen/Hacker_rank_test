'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
'''


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
import random

# solution 1: intuitive solution, slow and exceed time limitation for the final test......
class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.length = sum(self.w) - 1
        self.array = []
        for i, c in enumerate(self.w):
            [self.array.append(m) for m in [i] * c]

    def pickIndex(self):
        """
        :rtype: int
        """
        return self.array[random.randint(0, self.length)]


# solution 2
class Solution(object):

    def __init__(self, w):

        self.array = []
        start = 0
        for c in w:
            self.array.append([start, start + c])
            start += c
        self.len = len(w) - 1
        self.index_range = sum(w) - 1

    def pickIndex(self):

        left = 0;
        right = self.len
        random_index = random.randint(0, self.index_range)

        while 0 <= left <= right:

            i = (left + right) // 2

            if self.array[i][0] <= random_index < self.array[i][1]:
                return i

            elif random_index > self.array[i][0]:
                left = i + 1

            elif random_index <= self.array[i][1]:
                right = i - 1


# solution 3: fastest

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.ranges = []  # [0]*100
        self.store = [0] * 1000
        self.total = sum(w)
        # print(self.total)
        for i in range(len(w)):
            self.ranges.append(w[i] * 1000 / self.total)
        # print(self.ranges)
        j = 0
        for i, n in enumerate(self.ranges):
            for _ in range(n):
                self.store[j] = i
                j += 1
        # print(self.store)

    def pickIndex(self):
        """
        :rtype: int
        """
        return self.store[random.randrange(1000)]

# the 4th solution has same idea as above, in fact I think should even be faster
# but didnot pass the final test due to speed (exceed........) but why????????????????????????

class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.length = sum(self.w)
        self.array = [0] * self.length
        j = 0

        for i, c in enumerate(w):
            for _ in range(int(c)):
                self.array[j] = i
                j += 1

    def pickIndex(self):
        """
        :rtype: int
        """
        return self.array[random.randint(0, self.length-1)]


