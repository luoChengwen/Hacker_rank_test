class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        hashmap = dict()
        for i in dislikes:
            if i[0] not in hashmap:
                hashmap[i[0]] = 1

                if hashmap[i[1]] in hashmap:
                    if hashmap[i[1]] != -1: return False
            else:



        return True
 #
# dislikes = [[1,2],[1,3],[2,4]]
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]] ; N = 5
N = 10
dislikes = [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]
N = 5
[[1,2],[3,4],[4,5],[3,5]]