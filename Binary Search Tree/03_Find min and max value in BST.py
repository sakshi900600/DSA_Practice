
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def minValue(self, root):
        # code here
        if root == None:
            return None
        
        while root.left != None:
            root = root.left
        
        return root.data

    
    def maxValue(self,root):
        if root == None:
            return None
        
        while root.right != None:
            root = root.right

        return root.data

    
if __name__ == "__main__":
    # input:
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.right = Node(30)
    root.right.left = Node(15)

    # output:
    obj = Solution()
    print("Min value in BST is:", obj.minValue(root))
    print("Max value in BST is:", obj.maxValue(root))