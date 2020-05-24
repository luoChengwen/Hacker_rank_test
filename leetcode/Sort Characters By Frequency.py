'''
Sort Characters By Frequency
Solution
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

# solution 1
class Solution:
    def frequencySort(self, s: str) -> str:
        wd = dict()
        for i in s:
            if i in wd:
                wd[i] +=1
            else: wd[i] = 1

        wdsr = sorted(wd.items(), key= lambda x: x[1])
        print(wdsr)
        wdsr = wdsr[::-1]
        print(wdsr)
        output = []
        for m in range(len(wdsr)):
            i, v = wdsr[m]
            output.append(i*v)

        return ''.join(output)


# solution 2
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result =[]
        count = Counter(s)
        for ch, cnt in count.most_common():
            result += [ch]*cnt
        return ''.join(result)