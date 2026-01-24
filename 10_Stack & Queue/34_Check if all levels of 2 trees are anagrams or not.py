from typing import Optional
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None



class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        # code here
        
        if node1 == None or node2 == None:
            return False
        
        
        q1 = deque()
        q2 = deque()
        
        q1.append(node1)
        q2.append(node2)
        
        while q1 and q2:
            if len(q1) != len(q2):
                return False
                
            l1 = []
            l2 = []
            size = len(q1)
            
            for i in range(size):
                n1 = q1.popleft()
                n2 = q2.popleft()
                l1.append(n1.data)
                l2.append(n2.data)
                
                # n1
                if n1.left != None:
                    q1.append(n1.left)
                if n1.right != None:
                    q1.append(n1.right)
                
                # n2
                if n2.left != None:
                    q2.append(n2.left)
                if n2.right != None:
                    q2.append(n2.right)
                
            
            if self.anagram(l1, l2) == False:
                return False
            
        return True
        
        
        
    def anagram(self, l1, l2):
        if len(l1) != len(l2):
            return False
        
        # Way - 1
        # l1.sort()
        # l2.sort()
        
        # for i in range(len(l1)):
        #     if l1[i] != l2[i]:
        #         return False
        
        
        # Way-2
        dct1 = {}
        dct2 = {}
        
        for elem in l1:
            dct1[elem] = dct1.get(elem,0)+1
        
        for elem in l2:
            dct2[elem] = dct2.get(elem,0)+1
            
        
        # either compare 
        # for k in dct1:
        #     if dct1.get(k,0) != dct2.get(k,0):
        #         return False
        
        
        # return True
        
        # or simply return == coz in python it compared key,val both
        return dct1 == dct2
        
        
    
        
                
if __name__ == "__main__":   
    # Input:
    root1 = Node(1)
    root1.left = Node(3)
    root1.right = Node(2)
    root1.right.left = Node(5)
    root1.right.right = Node(4)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)

    sol = Solution()
    print(sol.areAnagrams(root1, root2))  
    # Output: True             
                
            
            
            
        
