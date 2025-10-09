class newNode:

    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printKSumPaths(root,k):
    if root == None:
        return
    
    path = []
    helper(root,path,k)


def helper(root,path,k):
    if root == None:
        return
    
    path.append(root.data)

    curr_sum = 0
    for i in range(len(path)-1, -1, -1):
        curr_sum += path[i]
        if curr_sum == k:
            print(path[i:])
    
    helper(root.left, path,k)
    helper(root.right, path,k)

    path.pop()



if __name__ == '__main__':

    root = newNode(1)
    root.left = newNode(3)
    root.left.left = newNode(2)
    root.left.right = newNode(1)
    root.left.right.left = newNode(1)
    root.right = newNode(-1)
    root.right.left = newNode(4)
    root.right.left.left = newNode(1)
    root.right.left.right = newNode(2)
    root.right.right = newNode(5)
    root.right.right.right = newNode(2)


    # input:
    k = 5
    printKSumPaths(root,k)

    # output:
    # [3, 2]
    # [1, 3, 1]
    # [3, 1, 1]
    # [4, 1]
    # [1, -1, 4, 1]
    # [-1, 4, 2]
    # [5]
    # [1, -1, 5]

