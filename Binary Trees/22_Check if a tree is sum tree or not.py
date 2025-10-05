class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def is_sum_tree(self, node):
        
        def helper(node):
            if node is None:
                return True, 0

            # Leaf node is a sum tree
            if node.left is None and node.right is None:
                return True, node.data

            # Recurse for left and right subtrees
            leftIsSum, leftSum = helper(node.left)
            rightIsSum, rightSum = helper(node.right)

            # Current node satisfies sum tree property?
            if leftIsSum and rightIsSum and node.data == leftSum + rightSum:
                # Return True and total sum including current node
                return True, node.data + leftSum + rightSum
            else:
                return False, 0

        isSum, _ = helper(node)  
        return isSum


if __name__ == "__main__":
    # input:
    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    # Output: True
    sol = Solution()
    print(sol.is_sum_tree(root))  
