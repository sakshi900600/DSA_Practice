
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


from collections import deque
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        q = deque()
        dct = {}
        q.append((root,0))
        
        while q:
            node,hd = q.popleft()
            
            if hd not in dct:
                dct[hd] = node.data
                
            if node.left != None:
                q.append((node.left,hd-1))
                
            if node.right != None:
                q.append((node.right, hd+1))
        
        
        sorted_keys = sorted(dct.keys())
        ans = []
        for i in sorted_keys:
            ans.append(dct[i])
        
        
        return ans
        
                
                
                

if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    sol = Solution()
    # output:
    # [2, 3, 5, 6]
    
    print(sol.topView(root))