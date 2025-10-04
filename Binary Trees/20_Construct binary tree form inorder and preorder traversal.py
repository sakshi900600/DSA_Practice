
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None



class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        index = [0]
        
        def helper(start,end):
            if start > end:
                return
            
            curr_val = preorder[index[0]]
            node = Node(curr_val)
            index[0] += 1
            
            if start == end:
                return node
                
            # node pos in inorder
            pos = inorder.index(curr_val)
            
            node.left = helper(start, pos-1)
            node.right = helper(pos+1, end)
            
            return node
        
        
        return helper(0,len(inorder)-1)
    

    def inorder(self,root):
        if root == None:
            return
        
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
        
        

if __name__ == "__main__":
    # input :
    inorder = [4, 2, 5, 1, 6, 3]
    preorder = [1, 2, 4, 5, 3, 6]
    
    sol = Solution()
    root = sol.buildTree(inorder, preorder)

    # output :
    # 4 2 5 1 6 3 
    sol.inorder(root)  
    
    
    