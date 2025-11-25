
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def search(self, root, key):
        # code here
        
        if root == None:
            return False
        
        found = False
        while root != None:
            if root.data == key:
                found = True
                break
            elif root.data < key:
                root = root.right
            else:
                root = root.left
        
        return found
        

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    key = 2

    # output: True
    obj = Solution()
    print(obj.search(root, key))