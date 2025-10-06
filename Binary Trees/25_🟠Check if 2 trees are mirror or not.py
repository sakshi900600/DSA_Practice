
# ques at the link were something else.....


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None



class Solution:

    # iterative approach
    def areMirror(self, a, b):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        #code here
        
        if a == None and b == None:
            return True
        
        if a == None or b == None:
            return False
            
        st1 = []
        st2 = []
        st1.append(a)
        st2.append(b)
        
        
        while st1 and st2:
            curr1 = st1.pop()
            curr2 = st2.pop()
            
            if curr1.data != curr2.data:
                return False
            
            if curr1.left and curr2.right:
                st1.append(curr1.left)
                st2.append(curr2.right)
            elif curr1.left or curr2.right:
                return False
        
            
            if curr1.right and curr2.left:
                st1.append(curr1.right)
                st2.append(curr2.left)
            elif curr1.right or curr2.left:
                return False
        
        
        return not st1 and not st2
        

    # recursive approach
    def areMirror_rec(self, a, b):
        '''
        :param root1,root2: two root of the given trees.
        :return: True False
        
        '''
        #code here
        
        if a == None and b == None:
            return True
        
        if a == None or b == None:
            return False
            
        
        return (a.data == b.data) and self.areMirror(a.left, b.right) and self.areMirror(a.right, b.left)
        


if __name__ == "__main__":
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)

    b = Node(1)
    b.left = Node(3)
    b.right = Node(2)
    b.right.left = Node(5)
    b.right.right = Node(4)

    obj = Solution()
    if obj.areMirror(a, b):
        print("Yes")
    else:
        print("No")

    if obj.areMirror_rec(a, b):
        print("Yes")
    else:
        print("No")