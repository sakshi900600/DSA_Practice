
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def getCount(self, root, l, h):
        # Your code here
        
        if root == None:
            return 0
        
        if root.data < l:
            return self.getCount(root.right, l,h)
        elif root.data > h:
            return self.getCount(root.left, l,h)
        else:
            return 1 + self.getCount(root.right, l,h) +  self.getCount(root.left, l,h)



if __name__ == "__main__":
    # Input:
    root = Node(10)
    root.left = Node(5)
    root.right = Node(50)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.right = Node(100)

    l = 5
    h = 45

    # Output: 3
    solution = Solution()
    count = solution.getCount(root, l, h)
    print(count)  