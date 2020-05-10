'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.



Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
'''

# solution 1 - use dictionary
class Solution:
    def findJudge(self, N: int, trust) -> int:

        trust_tdict = dict()

        for i in range(len(trust)):
            trustee = trust[i][0]
            trusted = trust[i][1]

            if trustee not in trust_tdict:
                trust_tdict[trustee] = -1
            else:
                trust_tdict[trustee] -= 1

            if trusted not in trust_tdict:
                trust_tdict[trusted] = 1
            else:
                trust_tdict[trusted] += 1

        for i in trust_tdict:
            if trust_tdict[i] == N-1:
                return i

        return -1


from collections import defaultdict
# solution 2 - set
class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1:
            return 1
        people = defaultdict(set) # could also define a list
        k = set()
        for p, j in trust:
            people[j].add(p)    # if list, should be append
            k.add(p)

        for i in people:
            if len(people[i]) == N - 1 and i not in k:
                return i
        return -1