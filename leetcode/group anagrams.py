'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''


# approach 1 : intuitive but slow
class Solution:
    def groupAnagrams(self, strs):

        listset = []
        final_output = []

        for i in range(len(strs)):
            set_ind = set(strs[i])

            if set_ind not in listset:
                listset.append(set_ind)
                final_output.append([strs[i]])
                continue

            for j in range(len(listset)):
                added = False
                if set_ind == listset[j]:
                    if sorted(strs[i]) == sorted(final_output[j][0]):
                        final_output[j].append(strs[i])
                        added = True
                        break

            if not added:
                final_output.append([strs[i]])
                listset.append(set_ind)

        return final_output


# solution 2: use of dictionary

class Solution:
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in strs:
            key = "".join(sorted(i))

            if key not in dict1:
                dict1[key] = [i]
            else:
                dict1[key].append(i)

        return list(dict1.values())

