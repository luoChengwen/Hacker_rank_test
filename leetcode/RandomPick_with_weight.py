


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
        for i, c in enumerate(w):
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