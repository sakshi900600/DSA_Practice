from collections import deque
class Solution(object):

    # TlE - here we are checking for next_word in wordList and in list searching tc is o(n) which will takes lots of time for all the words check. so need to optimize it.
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # applying bfs
        q = deque()
        q.append((beginWord, 1)) #(beingword, level)

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + ch + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        q.append((next_word, level+1))
        
        return 0


    def ladderLength_opt(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordList_set = set(wordList)
        # applying bfs
        q = deque()
        q.append((beginWord, 1)) #(beingword, level)

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + ch + word[i+1:]
                    if next_word in wordList_set:
                        wordList_set.remove(next_word)
                        q.append((next_word, level+1))
        
        return 0



if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    sol = Solution()
    # print(sol.ladderLength(beginWord, endWord, wordList)) 
    # Output: 5
    print(sol.ladderLength_opt(beginWord, endWord, wordList)) 
    # Output: 5
    

