
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

## inuitive approach, use dictionary
class Solution:
    def canConstruct(self, ransomNote, magazine) -> bool:
        note = dict()
        mag = dict()
        for i in range(len(ransomNote)):
            key = ransomNote[i]

            if key not in note:
                note[key] = 1
                mag[key] = 0
            else:
                note[key] += 1

        for j in magazine:
            if j in mag:
                mag[j] += 1

        for i in note:

            if note[i] > mag[i]:
                return False

        return True


# solution 2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
