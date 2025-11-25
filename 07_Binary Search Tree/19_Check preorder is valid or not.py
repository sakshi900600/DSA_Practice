
# def canRepresentBST(pre, n):
#     stack = []
#     root = float('-inf')
#     for i in range(n):
#         if pre[i] < root:
#             return False
#         while stack and stack[-1] < pre[i]:
#             root = stack.pop()
#         stack.append(pre[i])
#     return True


# # Example 
# n = 5
# preorder = [40, 30, 35, 80, 100]
# print(canRepresentBST(preorder, n))


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# the ques on given link is to create tree from preorder
def createBST(pre):

    def helper(pre, idx, minBound, maxBound):
        if idx[0] >= len(pre):
            return None
        
        val = pre[idx[0]]
        if val <= minBound or val >= maxBound:
            return None
        
        root = Node(val)
        idx[0] += 1

        if idx[0] < len(pre):
            root.left = helper(pre, idx, minBound, val)
        
        if idx[0] < len(pre):
            root.right = helper(pre, idx, val, maxBound)
        
        return root
    
    idx = [0]
    return helper(pre, idx, float('-inf'), float('inf'))



def inorder(root):
    if root == None:
        return root
    
    inorder(root.left)
    print(root.data , end=' ')
    inorder(root.right)


if __name__ == "__main__":

    pre = [10, 5, 1, 7, 40, 50]
    root = createBST(pre)

    # output: 
    # 1 5 7 10 40 50 
    inorder(root)