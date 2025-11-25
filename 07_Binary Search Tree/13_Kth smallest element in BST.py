
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # inorder logic
    def kthSmallest(self, root, k): 
        # code here
        
        def inorder(root,li):
            if root == None:
                return
            
            inorder(root.left, li)
            li.append(root.data)
            inorder(root.right, li)
        
        
        li = []
        inorder(root, li)
        
        if k > len(li):
            return -1
            
        return li[k-1]

    # stack logic:
    def kthSmallest_stack(self, root, k):
        st = [] # stack
        count = 0
        temp = root

        while st or temp != None:
            while temp != None:
                st.append(temp)
                temp = temp.left

            curr = st.pop()
            count += 1
            if count == k:
                return curr.data

            temp = curr.right

        return -1



            
if __name__ == "__main__":
    # input:
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    k = 3

    # Output: 40
    sol = Solution()
    print(sol.kthSmallest(root, k))
    print(sol.kthSmallest_stack(root, k))