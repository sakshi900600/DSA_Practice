
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # we know that inorder traversal of BST gives sorted order.
    def isBST(self, root):
        #code here
        
        li = []
        
        def inorder(root):
            if root == None:
                return None
            
            inorder(root.left)
            li.append(root.data)
            inorder(root.right)
        
        inorder(root)
        
        for i in range(len(li)-1):
            if li[i] > li[i+1]:
                return False
        
        return True
            


if __name__ == "__main__":

    # input:
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    

    # output:  True
    obj = Solution()
    print(obj.isBST(root))  
