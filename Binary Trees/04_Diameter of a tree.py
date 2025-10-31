
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def diameter(self, root):
        maxi = [float('-inf')]
    
        def height(root):
            if root is None:
                return 0
            
            lh = height(root.left)
            rh = height(root.right)
            
            # Update the diameter for every node
            maxi[0] = max(maxi[0], lh + rh)
            
            return 1 + max(lh, rh)
            
        
        height(root)
        return maxi[0]



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