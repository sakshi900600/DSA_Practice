#User function Template for python3

class TrieNode:
    def __init__(self):
        self.list = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        # implement Trie
        self.root = TrieNode()
        
        
    def insert(self, word: str):
        # insert word into Trie
        curr = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            
            if curr.list[idx] == None:
                newNode = TrieNode()
                curr.list[idx] = newNode
                
            curr = curr.list[idx]
        
        curr.isEndOfWord = True
       

    def search(self, word: str) -> bool:
        # search word in the Trie
        curr = self.root
        
        for ch in word:
            idx = ord(ch)-ord('a')
            
            if curr.list[idx] == None:
                return False
            
            curr = curr.list[idx]
        
        return curr.isEndOfWord
         

    def isPrefix(self, word: str) -> bool:
        # search prefix word in the Trie
        curr = self.root
        
        for ch in word:
            idx = ord(ch) - ord('a')
            
            if curr.list[idx] == None:
                return False
            
            curr = curr.list[idx]
        
        return True
        



if __name__ == "__main__":
    # Create a new Trie
    trie = Trie()
    
    # Test insert and search
    words_to_insert = ["apple", "app", "apricot","bat", "cat"]
    
    print("Inserting words:", words_to_insert)
    for word in words_to_insert:
        trie.insert(word)
    
    
    # Test search functionality
    print("\nTesting Search:")
    test_words = ["app", "apricot", "ball", "ap"]
    
    for word in test_words:
        found = trie.search(word)
        print(f"Search '{word}': {found}")
    
    
    # Test prefix functionality
    print("\nTesting Prefix:")
    test_prefixes = ["ap", "ba", "cata"]
    
    for prefix in test_prefixes:
        is_prefix = trie.isPrefix(prefix)
        print(f"Is '{prefix}' a prefix? {is_prefix}")
    
    
    # Additional test: Insert duplicate word
    print("\nTesting duplicate insertion:")
    trie.insert("apple")
    print("Inserted 'apple' again")
    print(f"Search 'apple': {trie.search('apple')}")
    
    