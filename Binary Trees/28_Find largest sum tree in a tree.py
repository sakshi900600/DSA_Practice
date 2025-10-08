from typing import Optional
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        # code here
        
        ans = [float('-inf')]
        
        def helper(root, ans):
            if root == None:
                return 0
            
            left_sum = helper(root.left, ans)
            right_sum = helper(root.right, ans)
            
            curr_sum = root.data + left_sum + right_sum
            ans[0] = max(ans[0], curr_sum)
            
            return curr_sum
        
        helper(root,ans)
        return ans[0]
        


if __name__ == "__main__":
    # input:
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(-6)
    root.right.right = Node(2)

    # output: 7
    sol = Solution()
    print(sol.findLargestSubtreeSum(root))
        
        
        
        
