
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        # code here
        
        def inorder(root, inord):
            if root == None:
                return
            
            inorder(root.left, inord)
            inord.append(root.data)
            inorder(root.right, inord)
        
        
        def replace_val(root, inord, idx):
            if root == None:
                return 
            
            replace_val(root.left, inord, idx)
            
            root.data = inord[idx[0]]
            idx[0] += 1
            
            replace_val(root.right, inord, idx)
            
            
        inord = []
        inorder(root, inord)  
        
        inord.sort()
        idx = [0]
        
        replace_val(root, inord, idx)
        
        return root
            
    

if __name__ == "__main__":
    # Example usage:
    root = Node(10)
    root.left = Node(30)
    root.right = Node(20)
    root.left.left = Node(5)
    root.left.right = Node(15)

    solution = Solution()
    bst_root = solution.binaryTreeToBST(root)

    # output: 5 10 15 20 30

    
    def print_inorder(node):
        if node is None:
            return
        print_inorder(node.left)
        print(node.data, end=' ')
        print_inorder(node.right)

    print("Inorder traversal of the converted BST:")
    print_inorder(bst_root)