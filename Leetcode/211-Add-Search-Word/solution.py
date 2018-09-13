# the only difference between this problem and a normal Trie tree is about the handle for '.'.
# use a flag = False, and for each children, compare child result OR with the flag to reflect availability. 

from collections import defaultdict
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.end = False
        self.children = defaultdict(lambda: WordDictionary)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self
        for c in word:
            if c not in curr.children:
                node = WordDictionary()
                curr.children[c] = node
            curr = curr.children[c]
        curr.end = True
        
    # do we have other methods except for recursion?
    def find_word_from_node(self, node, word):
        # print node.end, node.children, word
        curr = node
        for c in word:
            if c!= '.' and c not in curr.children:
                return False
            elif c == '.':
                for k, v in curr.children.iteritems():
                    if self.find_word_from_node(v, word[1:]):
                        return True
                return False
            return self.find_word_from_node(curr.children[c], word[1:])
        return True if curr.end else False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find_word_from_node(self, word)
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
print obj.search('b..')