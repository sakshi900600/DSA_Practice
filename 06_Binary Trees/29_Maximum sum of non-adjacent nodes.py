
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def getMaxSum(self, root):
        #code here
        if root == None:
            return 0
        
        def helper(root):
            if root == None:
                return (0,0) # (include, exclude)
            
            if root.left == None and root.right == None:
                return (root.data, 0)
            
            left_inc, left_exc = helper(root.left)
            right_inc, right_exc = helper(root.right)
            
            include = root.data + left_exc + right_exc
            exclude = max(left_inc, left_exc) + max(right_inc, right_exc)
            
            return (include, exclude)
            
        
        include, exclude = helper(root)
        return max(include, exclude)
        
        
            
            
if __name__ == "__main__":

    # input:
    root = Node(10)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)


    # Output: 22  
    sol = Solution()
    print(sol.getMaxSum(root))  
                