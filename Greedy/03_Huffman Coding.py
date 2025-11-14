#User function Template for python3


import heapq
class Solution:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
        
        # heapq uses < operator to compare two objects and sort them
        def __lt__(self, other):
            return self.data < other.data
            
    
    
    def huffmanCodes(self,S,f,N):
        # Code here
        pq = []
        
        for freq in f:
            node = self.Node(freq)
            heapq.heappush(pq, node)
        
        
        # connecting nodes
        while len(pq) > 1:
            node1 = heapq.heappop(pq)
            node2 = heapq.heappop(pq)
            
            newNode = self.Node(node1.data + node2.data)
            newNode.left = node1
            newNode.right = node2
            
            heapq.heappush(pq, newNode)
        
        
        # get code values of each leaf node
        root = heapq.heappop(pq)
        ans = []
        self.preorder(root, ans, "")
        
        return ans
    
    
    def preorder(self, root, ans, code):
        if root == None:
            return
        if root.left == None and root.right == None:
            ans.append(code)
        
        self.preorder(root.left, ans, code+'0')
        self.preorder(root.right, ans, code+'1')
    
    
        
            
if __name__ == "__main__":
    
    S = ['a', 'b', 'c', 'd', 'e', 'f']
    f = [5, 9, 12, 13, 16, 45]
    N = len(S)
    

    # Output: ['0', '100', '101', '1100', '1101', '111']
    sol = Solution()
    print(sol.huffmanCodes(S, f, N))
    