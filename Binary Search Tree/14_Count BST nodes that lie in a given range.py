
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def countPairs(self, root1, root2, x): 
        # code here
        
        if root1 == None or root2 == None:
            return None
        
        def inorder(root, li):
            if root == None:
                return
            
            inorder(root.left, li)
            li.append(root.data)
            inorder(root.right, li)
        
        
        a1 = []
        a2 = []
        
        inorder(root1, a1)
        inorder(root2, a2)
        
        # now find pair sum in both list.
        si = 0
        ei = len(a2)-1
        count = 0
        
        while si < len(a1) and ei >= 0:
            sum = a1[si] + a2[ei]
            if sum == x:
                count += 1
                si += 1
                ei -= 1
            elif sum < x:
                si += 1
            else:
                ei -= 1
                
        return count
            
        

if __name__ == "__main__":
    # input
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(7)
    
    root2 = Node(10)
    root2.left = Node(6)
    root2.right = Node(15)
    
    x = 11
    
    # output: 1
    sol = Solution()
    result = sol.countPairs(root1, root2, x)
    print(result)