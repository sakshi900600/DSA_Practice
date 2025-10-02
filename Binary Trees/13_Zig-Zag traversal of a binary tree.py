
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        # code here
        
        q = deque()
        ans = []
        reverse = False
        q.append(root)
        
        while q:
            temp = []
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                temp.append(node.data)
                
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                 
                    
            if reverse:
                temp.reverse()
            
            # ans.extend(temp)
            # or we can do this:
            ans += temp
            reverse = not reverse
        
        return ans
            
                    
                

if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    sol = Solution()
    # output:
    # [5, 6, 3, 2, 4]
    
    print(sol.zigZagTraversal(root))