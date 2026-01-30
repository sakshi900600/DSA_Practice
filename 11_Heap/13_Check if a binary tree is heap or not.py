
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def isHeap(self, root):
        # code Here
        
        q = deque()
        q.append(root)
        isleaf = False
        
        while q:
            node = q.popleft()
            
            if node.left != None:
                if isleaf or node.left.data > node.data:
                    return False
                q.append(node.left)
            else:
                isleaf = True
            
            if node.right != None:
                if isleaf or node.right.data > node.data:
                    return False
                q.append(node.right)
            else:
                isleaf = True
        
        
        return True
        
        
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(9)
    root.right = Node(8)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

    sol = Solution()
    print(sol.isHeap(root))  # Output: True
            
            
