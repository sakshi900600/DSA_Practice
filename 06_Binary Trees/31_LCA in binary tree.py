
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def lca(self, root, n1, n2):
        # code here
        
        # store parents for each node    
        parent_dct = {}
        q = deque()
        q.append((root, None))
        
        while q:
            node,parent = q.popleft()
            
            if node not in parent_dct:
                parent_dct[node] = parent
            
            if node.left != None:
                q.append((node.left, node))
            
            if node.right != None:
                q.append((node.right, node))
        
        
        node1 = None
        node2 = None
        
        for node in parent_dct:
            if node.data == n1:
                node1 = node
            if node.data == n2:
                node2 = node
                
        
        # store ancestors of node 1
        li = [] # ancestors
        while node1 != None:
            li.append(node1)
            node1 = parent_dct[node1]
        
        
        while node2 != None:
            if node2 in li:
                return node2
            
            node2 = parent_dct[node2]
        
            
        
        
        
if __name__ == "__main__":

    # input:
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)


    # Output: 3  
    sol = Solution()
    print(sol.lca(root, 5, 1).data)