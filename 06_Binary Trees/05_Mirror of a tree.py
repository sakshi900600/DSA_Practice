class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    

def mirror_inplace(root):
    if root == None:
        return 
        
    root.left , root.right = root.right, root.left
    mirror_inplace(root.right)
    mirror_inplace(root.left)
    




if __name__ == '__main__':

    # input:
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)


    # output:
    # 2 3 4 5 6 

    # 6 5 4 3 2

    inorder(root)
    print("\n")
    # mirror_inplace(root)
    mirror_new(root)
    inorder(root)
