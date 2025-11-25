class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        #your code here
        
        st = [] #stack
        count = 0
        temp = root
        
        while st or temp != None:
            while temp != None:
                st.append(temp)
                temp = temp.right
            
            curr = st.pop()
            count += 1
            if count == k:
                return curr.data
            
            temp = curr.left
        
        return -1
        
            
if __name__ == "__main__":
    # Example usage:
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    k = 3

    # Output: 60
    sol = Solution()
    print(sol.kthLargest(root, k))  
