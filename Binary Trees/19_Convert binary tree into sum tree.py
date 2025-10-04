
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def toSumTree(self, root) :
        #code here
        
        if root == None:
            return 0
        
        left_data = self.toSumTree(root.left)
        right_data = self.toSumTree(root.right)
        
        curr_data = root.data
        new_data = left_data + right_data
        
        root.data = new_data
        return curr_data + new_data


    def inorder(self,root):
        if root == None:
            return
        
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


if __name__ == "__main__":
    # input:
    root = Node(10)
    root.left = Node(-2)
    root.right = Node(6)
    root.left.left = Node(8)
    root.left.right = Node(-4)
    root.right.left = Node(7)
    root.right.right = Node(5)

    sol = Solution()
    # output:
    # 0 4 0 20 0 12 0 
    
    sol.toSumTree(root)
    sol.inorder(root)