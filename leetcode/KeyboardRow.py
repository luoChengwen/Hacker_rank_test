'''
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.
'''

# easy level, should add in the instruction that capital and small do not matter

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'

        to_keep = []

        for word in words:
            word1 = word.lower()
            if word1[0] in row1: to_comp = row1
            elif word1[0] in row2: to_comp = row2
            else: to_comp = row3

            to_keep.append(word)

            for i in word1[1:]:
                if i not in to_comp:
                    to_keep.remove(word)
                    break
        return to_keep