
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Solution:
    def LCA(self, root, n1, n2):
        # code here
        
        if root == None:
            return None
        
        while root:
            if root.data==n1.data or root.data==n2.data:
                return root
            elif root.data>n1.data and root.data>n2.data:
                root = root.left
            elif root.data<n1.data and root.data<n2.data:
                root = root.right
            else:
                return root
              
    
        
        
if __name__ == "__main__":

    # BST input:
    #       10
    #      /  \
    #     5    15
    #    / \    / \
    #   3   7  12  18

    # node1 =5, node2 =15

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)


    # Output: 10  
    sol = Solution()
    print(sol.LCA(root, root.left, root.right).data)