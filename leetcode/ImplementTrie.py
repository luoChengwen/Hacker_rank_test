'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''


# solution 1: first intuition is to use list, then append. I tried but this is slow.

# solution 2:
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordlist = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.wordlist
        for i in word:
            if i not in temp:
                temp[i] = dict()
            temp = temp[i]
        temp['#'] = True  #this is a nice mark indicating the end of the word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.wordlist
        for j in word:
            if j in temp:
                temp = temp[j]
            else:
                return False
            print(temp)
        return '#' in temp  # this is to check whether it is now the end of the word,
        # compare with starts with

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.wordlist
        for m in prefix:
            if m in temp:
                temp = temp[m]
            else:
                return False
        return True

