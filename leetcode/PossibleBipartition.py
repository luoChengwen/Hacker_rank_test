'''
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
'''

"""
:type N: int
:type dislikes: List[List[int]]
:rtype: bool
"""

''' depth first/ breath first search
'''
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        if len(dislikes) < 2: return True

        pairs = dict()

        for i,j in dislikes:
            i-=1 ; j-=1 # to match with the location whose index starting from 0
            if i not in pairs: pairs[i] = [j]
            else: pairs[i].append(j)
            if j not in pairs: pairs[j] = [i]
            else: pairs[j].append(i)

        color = [0] * N

        for i in range(N):
            if color[i] != 0: continue
            color[i] = 1
            queue = [i]

            while queue:
                current = queue.pop(0)

                try:
                    for element in pairs[current]:
                        if color[element] == 0:
                            color[element] = color[current] * -1
                            queue.append(element)
                        else:
                            if color[element] == color[current]:
                                return False
                except: pass

        return True
