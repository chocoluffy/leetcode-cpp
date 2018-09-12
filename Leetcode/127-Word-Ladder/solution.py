from collections import deque, defaultdict
class Solution(object):
    # runtime error.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        char_map = defaultdict(set)
        word_len = len(beginWord)
        N = len(wordList)
        queue = deque()
        level = 0
        queue.append(beginWord)
        visited = [False] * N
        while len(queue) > 0:
            size = len(queue)
            level += 1
            while(size > 0):
                size -= 1
                curr = queue.popleft()
                #find valid sucessor nodes: 1) 1 transformation. 2) in wordList
                for i in range(word_len):
                    if len(char_map[i]) == 0: # init
                        char_map[i] = set(map(lambda x: x[i], wordList))
                    for c in char_map[i]:
                        if c == curr[i]: # not tranform to itself
                            continue
                        else:
                            new_word = curr[:i] + c + curr[i+1:]
                            if new_word in wordList:
                                if new_word == endWord:
                                    return level + 1
                                else:
                                    # print new_word, visited[wordList.index(new_word)]
                                    if not visited[wordList.index(new_word)]:
                                        visited[wordList.index(new_word)] = True
                                        queue.append(new_word)
        return 0
                