class TrieNode:
    def __init__(self):
        self.childern = [None]*26
        self.isEndOfWord = False

    
    def insert(root, key):
        curr = root

        for ch in key:
            idx = ord(ch)-ord('a')

            if curr.childern[idx] == None:
                newNode = TrieNode()
                curr.childern[idx] = newNode

            curr = curr.childern[idx]

        curr.isEndOfWord = True

    
    def search(root, key):
        curr = root
        
        for ch in key:
            idx = ord(ch) - ord('a')

            if curr.childern[idx] == None:
                return False
            
            curr = curr.childern[idx]

        return curr.isEndOfWord
    


