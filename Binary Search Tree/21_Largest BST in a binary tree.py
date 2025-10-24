class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class BSTInfo:
    def __init__(self, mini, maxi, size):
        self.mini = mini
        self.maxi = maxi
        self.size = size


class Solution:
    
    def largestBst(self, root):
        # Your code here
        
        def helper(root):
            if root == None:
                return BSTInfo(float('inf'), float('-inf'), 0)
            
            left = helper(root.left)
            right = helper(root.right)
            
            # if valid bst
            if left.maxi < root.data and right.mini > root.data:
                min_val = min(root.data, left.mini)
                max_val = max(root.data, right.maxi)
                max_size = 1 + left.size + right.size
                
                return BSTInfo(min_val, max_val, max_size)
            
            
            # if not valid bst then store max size
            return BSTInfo(float('-inf'), float('inf'), max(left.size, right.size))
            
        
        return helper(root).size
            
            
            

if __name__ == "__main__":
    root = Node(6)
    root.left = Node(7)
    root.right = Node(3)
    root.left.right = Node(2)
    root.right.left = Node(2)
    root.right.right = Node(4)

    # Output: 3
    ob = Solution()
    print(ob.largestBst(root))  
