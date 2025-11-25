
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    
    def morrisInorder(self, root):
        curr = root
        ans = []
        
        while curr != None:
            if curr.left == None:
                ans.append(curr.data)
                curr = curr.right
            else:
                # get left subtree rightmost node and connect it
                pred = curr.left
                while pred.right != None and pred.right != curr:
                    pred = pred.right
                
                if pred.right == None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    ans.append(curr.data)
                    curr = curr.right
                    
        return ans
                
                
                
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)

    sol = Solution()
    print(sol.morrisInorder(root))

    # output:  [1, 2, 3, 4, 6]