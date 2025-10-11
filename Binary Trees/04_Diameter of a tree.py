
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def diameter(self, root):
        self.maxi = 0
        self.height(root)
        return self.maxi
    
    def height(self, root):
        if root is None:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        # Update the diameter for every node
        self.maxi = max(self.maxi, lh + rh)
        
        return 1 + max(lh, rh)


if __name__ == "__main__":
    # input
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)
    root.left.left.right = Node(7)

    # output: 4
    sol = Solution()
    print(sol.diameter(root))