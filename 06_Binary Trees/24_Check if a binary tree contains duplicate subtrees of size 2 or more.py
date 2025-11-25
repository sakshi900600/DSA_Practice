
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def dupSub(self, root):
        # code here
        
        # steps: 
        # 1. searilize tree(store tree in the form of string)
        # 2. store freq in dct
        # 3. if freq == 2 and len of serial string > 3 store true
        # 4. return serial string from helper fun.
        
        
        dct = {}
        isDuplicate = [0]
        
        def helper(root):
            if root == None:
                return '#' # leaf nodes
            
            left = helper(root.left)
            right = helper(root.right)
            
            serial_str = f"{root.data},{left},{right}"
            
            dct[serial_str] = dct.get(serial_str, 0) + 1
            
            if dct[serial_str] == 2 and len(serial_str.split(',')) > 3:
                isDuplicate[0] = 1
                
            
            return serial_str
            
        
        helper(root)
        return isDuplicate[0]
            
            
            

if __name__ == "__main__":

    # input:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(2)
    root.right.left.left = Node(4)
    root.right.right = Node(4)

    # Output: 1
    obj = Solution()
    print(obj.dupSub(root))   
