
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        
        if root == None:
            return -1
            
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        return 1+ max(lh,rh)




if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    sol = Solution()
    

    # output: 2
    
    print(sol.height(root))