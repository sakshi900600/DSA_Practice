
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findPreSuc(self, root, key):
        # code here
        
        predecessor = None
        successor = None
        
        while root != None:
            if root.data < key:
                predecessor = root
                root = root.right
            elif root.data > key:
                successor = root
                root = root.left
            else:
                if root.left != None:
                    predecessor = self.left_rightMost(root.left)
                
                if root.right != None:
                    successor = self.right_leftMost(root.right)
                
                return [predecessor, successor]
        
        return [predecessor, successor]
                
        
        
    def left_rightMost(self, root):
        while root.right != None:
            root = root.right
        return root
        
        
    def right_leftMost(self, root):
        while root.left != None:
            root = root.left
        return root
            
            
        
if __name__ == "__main__":

    # input:
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    key = 65

    # output:
    # Predecessor: 60
    # Successor: 70

    
    sol = Solution()
    pre, suc = sol.findPreSuc(root, key)
    
    if pre:
        print("Predecessor:", pre.data)
    else:
        print("Predecessor: None")
    
    if suc:
        print("Successor:", suc.data)
    else:
        print("Successor: None")
                
                
            