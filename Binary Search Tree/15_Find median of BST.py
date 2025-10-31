
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def findMedian(self, root):
        # code here
        # no of nodes
        
        n = self.morrisInorder(root)
        
        if n % 2 == 0:
            medianIdx = n // 2
        else:
            medianIdx = (n+1) //2
        
        
        curr = root
        node_count = 0
        
        while curr != None:
            if curr.left == None:
                node_count += 1
                if node_count == medianIdx:
                    return curr.data
                
                curr = curr.right
            else:
                pred = curr.left
                while pred.right != None and pred.right != curr:
                    pred = pred.right
                
                if pred.right == None:
                    pred.right = curr
                    curr = curr.left
                else:
                    node_count += 1
                    if node_count == medianIdx:
                        return curr.data
                        
                    pred.right = None
                    curr = curr.right
        
        return -1
            
        
    
    def morrisInorder(self, root):
        curr = root
        count = 0
        
        while curr != None:
            if curr.left == None:
                count += 1
                curr = curr.right
            else:
                # get left subtree rightmost node and connect it
                pred = curr.left
                while pred.right != None and pred.right != curr:
                    pred = pred.right
                
                if pred.right == None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    count += 1
                    curr = curr.right
                    
        return count
                
                

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(1)

    # Output: 4
    sol = Solution()
    print(sol.findMedian(root))