
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def merge_BST(root1, root2):
    l1 = []
    l2 = []
    inorder(root1, l1)
    inorder(root2, l2)
    li = merge(l1, l2)

    return create_BST(0, len(li)-1, li)


def inorder(root, li):
    if root == None:
        return 
    inorder(root.left, li)
    li.append(root.data)
    inorder(root.right, li)


def merge(a,b):
    i = 0 # for array a
    j = 0 # for array b
    temp = []
    n = len(a)
    m = len(b)

    while i<n and j<m:
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
    
    while i<n:
        temp.append(a[i])
        i += 1
    
    while j < m:
        temp.append(b[j])
        j += 1
    
    return temp


def create_BST(si, ei, li):
    if si > ei:
        return None
    
    mid = (si+ei)//2
    root = Node(li[mid])
    
    root.left = create_BST(si, mid-1, li)
    root.right = create_BST(mid+1, ei, li)

    return root



if __name__ == "__main__":
    root1 = Node(30)
    root1.left = Node(20)
    root1.right = Node(40)
    root1.left.left = Node(10)

    root2 = Node(70)
    root2.left = Node(60)
    root2.right = Node(80)
    root2.right.left = Node(75)

    # merge BST fun call:
    merged_root = merge_BST(root1, root2)

    def print_inorder(root):
        if root is None:
            return
        print_inorder(root.left)
        print(root.data, end=' ')
        print_inorder(root.right)
    
    print_inorder(merged_root)