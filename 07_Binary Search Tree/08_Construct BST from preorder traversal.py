#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size) -> Node:
    #code here
    
    idx = [0]
    
    def helper(idx, pre, minBound, maxBound):
        if idx == len(pre):
            return None
        
        val = pre[idx[0]]
        if val <= minBound or val >= maxBound:
            return None
            
        root = Node(val)
        idx[0] += 1
        
        if idx[0] < len(pre):
            root.left = helper(idx, pre, minBound, val)
        
        if idx[0] < len(pre):
            root.right = helper(idx, pre, val, maxBound)
    
        
        return root
        
        
    return helper(idx, pre, float('-inf'), float('inf'))


def inorder(root):
    if root == None:
        return root
    
    inorder(root.left)
    print(root.data , end=' ')
    inorder(root.right)


if __name__ == "__main__":

    pre = [10, 5, 1, 7, 40, 50]
    size = len(pre)
    root = Bst(pre, size)

    # output: 
    # 1 5 7 10 40 50 
    inorder(root)