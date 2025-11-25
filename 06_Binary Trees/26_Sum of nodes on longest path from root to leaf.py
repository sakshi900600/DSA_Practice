
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None


class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
        
        def helper(root):
            if root == None:
                return (0,0) # height,sum
            
            if root.left == None and root.right == None:
                return (1, root.data)
            
            lh, ls = helper(root.left)
            rh, rs = helper(root.right)
            
            if lh > rh:
                return (1+lh, ls+root.data)
            elif rh > lh:
                return (1+rh, rs+root.data)
            else:
                return (1+lh, max(ls,rs)+root.data)
                
            
        
        return helper(root)[1]
            
            

if __name__ == "__main__":

    # input:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)

    # Output: 15 (7 + 4 + 2 + 1 + 1)
    sol = Solution()
    print(sol.sumOfLongRootToLeafPath(root))  