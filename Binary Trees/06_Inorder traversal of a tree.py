
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # using recursion: -----------------
    def inorder(self, root):
        # code here
        li = []
        self.helper(root,li)
        return li  
        
    def helper(self, root,li):
        # code here
        if root == None:
            return 

        self.helper(root.left,li)  
        li.append(root.data)
        self.helper(root.right,li)  


    # using iterative approach -------------------
    def inorder_it(self,root):
        st = []
        li = []
        node = root

        while True:
            if node != None:
                st.append(node)
                node = node.left
            
            else:
                if not st:
                    break
                
                visited_node = st.pop()
                li.append(visited_node.data)

                node = visited_node.right
            
        return li




if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(6)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(2)

    sol = Solution()
    # output:
    # [2, 3, 4, 5, 6]

    # print(sol.inorder(root))
    print(sol.inorder_it(root))
