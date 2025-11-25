
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def rightView(self,root):
        # code here
        
        if root == None:
            return []
        
        st = []
        dct = {}
        
        st.append((root,0))
        
        while st:
            node,level = st.pop()
            
            if level not in dct:
                dct[level] = node.data
                
            
            if node.left != None:
                st.append((node.left,level+1)) 
            
            if node.right != None:
                st.append((node.right,level+1))
              
                
        
        ans = []
        sorted_keys = sorted(dct.keys())
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
    # [5, 6, 4]
    
    print(sol.rightView(root))