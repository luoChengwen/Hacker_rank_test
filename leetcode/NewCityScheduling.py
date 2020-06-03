'''
Two City Scheduling
Solution
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
'''


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        # my idea is to order the differences first and then decide
        # how to schedule 
        difs = []
        N = len(costs)
        for i in range(N):
            difs.append([abs(costs[i][0] - costs[i][1]), i])

        difs.sort(key=lambda x: x[0], reverse=True)

        A = 0;
        B = 0
        sum_cost = 0
        i = 0
        while i < N:

            if costs[difs[i][1]][0] < costs[difs[i][1]][1] and A < N // 2:
                A += 1
                sum_cost += costs[difs[i][1]][0]
            elif B < N // 2:
                sum_cost += costs[difs[i][1]][1]
                B += 1
            else:
                sum_cost += costs[difs[i][1]][0]
            i += 1

        return sum_cost