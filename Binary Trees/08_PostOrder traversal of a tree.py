
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # using recursion: -----------------
    def postorder(self, root):
        # code here
        li = []
        self.helper(root,li)
        return li  
        
    def helper(self, root,li):
        # code here
        if root == None:
            return 

        self.helper(root.left,li)  
        self.helper(root.right,li)  
        li.append(root.data)


    # using iterative approach -------------------
    def postorder_it(self,root):
        st = []
        li = []

        st.append(root)
        while st:
            node = st.pop()
            li.append(node.data)

            if node.left != None:
                st.append(node.left)
            
            if node.right != None:
                st.append(node.right)

        li.reverse()
        return li
        

    

        
        
if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)

    sol = Solution()
    # output:
    # [2, 4, 3, 6, 5]
    
    # print(sol.postorder(root))
    print(sol.postorder_it(root))