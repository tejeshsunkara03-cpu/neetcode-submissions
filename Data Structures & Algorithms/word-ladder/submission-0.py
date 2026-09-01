from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)

        queue = deque([(beginWord, 1)])

        while queue:

            word, steps = queue.popleft()

            for i in range(len(word)):

                for char in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + char + word[i + 1:]

                    if newWord == endWord:
                        return steps + 1

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, steps + 1))

        return 0