class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """

        if root == None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            # node found
            if root.left==None and root.right==None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                # connect left subtree to right subtrees leftmost child node
                left_sub_head = root.left
                right_sub_head = root.right

                # finding right subtree leftmost node
                temp = right_sub_head
                while temp.left != None:
                    temp = temp.left
                
                temp.left = left_sub_head

                return right_sub_head

        
        return root


def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)



if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    key = 3

    # outputs:  
    inorder(root) # 2 3 4 5 6 7

    sol = Solution()
    new_root = sol.deleteNode(root, key)

    print()
    inorder(new_root) # 2 4 5 6 7