#User function Template for python3
class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.freq = 0


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
            
            curr = curr.links[idx]
            curr.freq += 1
        
    
    def getPrefix(self, word):
        curr = self.root
        
        for i in range(len(word)):
            ch = word[i]
            idx = ord(ch) - ord('a')
            
            if curr.links[idx].freq == 1:
                return i
                
            curr = curr.links[idx]
        
        return len(word)-1
            


class Solution:
    def findPrefixes(self, arr, N):
        # code here 
        
        trie = Trie()
        
        for i in range(N):
            trie.insert(arr[i])
        
        ans = []
        
        for i in range(N):
            word = arr[i]
            endIdx = trie.getPrefix(word)
            
            ans.append(word[:endIdx+1])
        
        return ans
        
        

if __name__ == "__main__":

    sol = Solution()
    arr = ["zebra", "dog", "duck", "dove"]
    n = len(arr)
    # Output:
    # ['z', 'dog', 'du', 'dov']

    print(sol.findPrefixes(arr,n))
