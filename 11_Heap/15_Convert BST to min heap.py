class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Solution:

    def bst_to_minHeap(self,root):

        inord = []
        def inorder(root):
            if root == None:
                return 
            
            inorder(root.left)
            inord.append(root.data)
            inorder(root.right)
        

        inorder(root)
        idx = [0]
        self.preorder_fill(root, inord, idx)

        return root

    
    def preorder_fill(self, root, inord, idx):
        if root == None:
            return 
        
        root.data = inord[idx[0]]
        idx[0] += 1

        self.preorder_fill(root.left, inord, idx)
        self.preorder_fill(root.right, inord, idx)




if __name__ == "__main__":

    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    sol = Solution()
    res = sol.bst_to_minHeap(root)

    # preorder
    def preorder(root):
        if root == None:
            return
        
        print(root.data, end="  ")
        preorder(root.left)
        preorder(root.right)


    preorder(res)
    # Output: 1  2  3  4  5  6  7  
        

