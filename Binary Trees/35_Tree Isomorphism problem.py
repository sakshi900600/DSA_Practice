class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        #code here.
        
        if root1==None and root2==None:
            return True
        
        if root1==None or root2==None:
            return False
        
        if root1.data != root2.data:
            return False
        
        # all possibilities: left,left and right,right match or left,right and right,left
        ll = self.isIsomorphic(root1.left, root2.left)
        rr = self.isIsomorphic(root1.right, root2.right)
        lr = self.isIsomorphic(root1.left, root2.right)
        rl = self.isIsomorphic(root1.right, root2.left)
        
        return (ll and rr) or (lr and rl)
        


if __name__ == "__main__":

     # Representation of input binary tree 1
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    #       / \
    #      7   8
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.right.left = Node(7)
    root1.left.right.right = Node(8)

    # Representation of input binary tree 2
    #        1
    #       / \
    #      3   2
    #     /   / \
    #    6   4   5
    #           / \
    #          8   7
    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.left.left = Node(6)
    root2.right.left = Node(4)
    root2.right.right = Node(5)
    root2.right.right.left = Node(8)
    root2.right.right.right = Node(7)


    # output: False
    sol = Solution()
    print(sol.isIsomorphic(root1, root2))