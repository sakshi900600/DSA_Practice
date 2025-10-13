class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def printAllDups(self, root):
        # code here
        
        freq = {}
        res = []
        
        def serialize(root):
            if root == None:
                return '#'
            
            left = serialize(root.left)
            right = serialize(root.right)
            
            serial_str = f"{root.data}, {left}, {right}"
            
            if serial_str in freq:
                freq[serial_str][0] += 1
            else:
                freq[serial_str] = [1, root]
                
            if freq[serial_str][0] == 2:
                res.append(root)
            
            return serial_str
            
            
        serialize(root)
        return res
        
        
        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(2)
    root.right.left.left = Node(4)
    root.right.right = Node(4)


    ob = Solution()
    duplicates = ob.printAllDups(root)
    
    # print(duplicates)

    # output: 4 2 

    for node in duplicates:
        print(node.data, end=" ")