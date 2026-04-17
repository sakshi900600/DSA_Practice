class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.cntEndWith = 0
        self.cntPrefix = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if curr.links[idx] == None:
                newNode = TrieNode()
                curr.links[idx] = newNode
            
            curr.cntPrefix += 1
            curr = curr.links[idx]
        
        curr.cntEndWith += 1


    def countWordsEqualTo(self, word):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if curr.links[idx] == None:
                return 0

            curr = curr.links[idx]
        
        return curr.cntEndWith
    


    def countWordStartingWith(self, word):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if curr.links[idx] == None:
                return 0
            
            curr = curr.links[idx]
        
        return curr.cntPrefix
        
    
    def erase(self, word):
        if self.countWordsEqualTo(word) == 0:
            return False
        
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            curr = curr.links[idx]
            curr.cntPrefix -= 1
        
        curr.cntEndWith -= 1

        return True
            


    