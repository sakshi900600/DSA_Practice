class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:

    def populateNext(self, root):
        
        li = []
        
        def inorder(root):
            if root == None:
                return None
            
            inorder(root.left)
            li.append(root)
            inorder(root.right)
        
        inorder(root)
        
        for i in range(len(li)-1):
            li[i].next = li[i+1]
        


if __name__ == "__main__":

    # input:
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(3)


    sol = Solution()
    sol.populateNext(root)

    curr = root.left.left  # Starting from the leftmost node
    while curr:
        if curr.next != None:
            print("Node = ", curr.data, "Next = ", curr.next.data)
        else:
            print("Node = ", curr.data, "Next = -1")
        curr = curr.next

    
    # output: 
    # Node =  3 Next =  8
    # Node =  8 Next =  10
    # Node =  10 Next =  12
    # Node =  12 Next = -1