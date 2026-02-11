# 1. compare words of dict and checks where the first letter differs,
# It can happpen that some char are already in the char list and nw char comes but it should come before some other char, so it will be messay in list to do it.

# So, here we will treat chars as a node and then create directed edge b/n them.
# Then apply khans algo, if it will give list of containing all unique chars present in wordList then ok return that otherwise it simply means that order is not possible.


# Steps:
# 1. find out all the unique char which exists in words. (mark in exists list)
# 2. traverse given wordslist and get the idx of the chars and add in adjlist also update indegree.
# 3. After creating graph (adjlist). apply khans algorithm.
# 4. here make sure to also check if ch exists when checking and putting 0 indegree char in q.
# 5. apply this algo
# 6. At the end check if the final toposort list contains all the chars that exists or not. If not then return "" othersiw join the list and return as a string.



from collections import deque
class Solution:
    def findOrder(self, words):
        # code here
        n = len(words)
        adj = [[] for _ in range(26)]
        indegree = [0]*26
        exists = [0]*26
        
        for word in words:
            for ch in word:
                idx = ord(ch)- ord('a')
                exists[idx] = 1
                
        
        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            
            minlen = min(len(word1), len(word2))
            j = 0
            while j<minlen and word1[j]==word2[j]:
                j += 1
            
            if j < minlen:
                ch1 = word1[j]
                ch2 = word2[j]
                
                u = ord(ch1) - ord('a')
                v = ord(ch2) - ord('a')
                adj[u].append(v)
                
                indegree[v] += 1
                
            elif len(word1) > len(word2):
                return ""
        
        q = deque()
        for i in range(26):
            if indegree[i] == 0 and exists[i]==1:
                q.append(i)
        
        ans = []
        
        while q:
            node = q.popleft() # char no
            ch = chr(node+ord('a'))
            ans.append(ch)
            
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        if len(ans) != sum(exists):
            return ""
            
            
        return "".join(ans)
                
            
        
        
                
if __name__ == "__main__":

    # ch = 'c'
    # print(ord('a')) # 97
    # print(ord(ch) - ord('a')) # 2
    # print(chr(2+ord('a'))) # c

    sol = Solution()
    words = ["baa", "abcd", "abca", "cab", "cad"]
    print(sol.findOrder(words))
    # Output: bdac

    words = ["ab", "cd", "ef", "ad"]
    print(sol.findOrder(words))
    # Outptu: ""
    