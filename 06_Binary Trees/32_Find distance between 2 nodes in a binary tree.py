
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def findDist(self,root,a,b):
    
        #return: minimum distance between a and b in a tree with given root
        #code here
        dist_n1 = self.get_level(root, a, 0)
        dist_n2 = self.get_level(root, b, 0)
        
        lca = self.LCA(root,a,b) # returns node
        lca_val = lca.data
        
        dist_lca_val = self.get_level(root, lca_val, 0)
        
        return dist_n1 + dist_n2 - 2 * dist_lca_val
        
        
        
    # get level of each node
    def get_level(self, root, target, level):
        if root == None:
            return -1
        
        if root.data == target:
            return level
        
        left_res = self.get_level(root.left, target, level+1)
        if left_res != -1:
            return left_res
    
        right_res = self.get_level(root.right, target, level+1)
        
        return right_res
        
        
    
    def LCA(self, root, n1, n2):
        # store parent list
        parent_dct = {}
        q = deque()
        q.append((root, None))
        
        while q:
            node, parent = q.popleft()
            
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
                
        
        li = [] # ancestors
        while node1:
            li.append(node1)
            node1 = parent_dct[node1]
        
        
        while node2:
            if node2 in li:
                return node2
            node2 = parent_dct[node2]
            
        
        

if __name__ == "__main__":

    # input:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    
    a = 4
    b = 5
    
    # output: 2
    obj = Solution()
    print(obj.findDist(root, a, b))   