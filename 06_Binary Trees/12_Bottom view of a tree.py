
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        q = deque()
        dct = {}
        q.append((root,0))
        
        while q:
            node,hd = q.popleft()
            
            if hd not in dct:
                dct[hd] = node.data
            else:
                dct[hd] = node.data
            
            
            if node.left != None:
                q.append((node.left,hd-1))
                
            if node.right != None:
                q.append((node.right,hd+1))
                
                
        sorted_keys = sorted(dct.keys())
        ans = []
        for i in sorted_keys:
            ans.append(dct[i])
            
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
    # [2, 3, 4, 6]
    
    print(sol.bottomView(root))