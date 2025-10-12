class newNode: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


from collections import deque

def kthAncestor(root, tnode, k):
    if root == None:
        return -1
    

    # build parent
    parent_dct = {}
    q = deque()
    q.append((root, None))

    while q:
        node,parent = q.popleft()

        if node not in parent_dct:
            parent_dct[node] = parent
        
        if node.left != None:
            q.append((node.left, node))
        if node.right != None:
            q.append((node.right, node))
    
    node1 = None
    for node in parent_dct:
        if node.data == tnode:
            node1 = node
            break
    

    if node1 == None:
        return -1
    
    while node1 and k >0:
        node1 = parent_dct[node1]
        k -= 1
    
    return node1.data if node1 else -1



if __name__ == '__main__':

    # input:
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 

    # note - k can't be 0 coz given k will be always +ve integer.
    k = 2
    node = 5

    # output: 1
    print(kthAncestor(root,node,k))