class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def isDeadEnd(self, root):
        # Code here
        
        def helper(root, minBound, maxBound):
            if root == None:
                return False
            
            if minBound == maxBound:
                return True
            
            left_res = helper(root.left, minBound, root.data-1)
            right_res = helper(root.right, root.data+1, maxBound)
            
            return left_res or right_res
        
        
        return helper(root, 1, float('inf'))

    

if __name__ == "__main__":

    # input
    root = Node(8)
    root.left = Node(5)
    root.right = Node(9)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.left.left.left = Node(1)
    root.left.left.right = Node(3)

    # output: True
    sol = Solution()
    print(sol.isDeadEnd(root))