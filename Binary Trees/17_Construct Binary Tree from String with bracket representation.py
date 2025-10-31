from typing import Optional
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def treeFromString(self, s : str) -> Optional['Node']:
        # code here
        if not s:
            return None
        
        n = len(s)
        i = 0
        # get the roots data. 
        while i<n and s[i].isdigit():
            i += 1
        
        root_data = s[:i]
        root = Node(root_data)
        
        if i >= n:
            return root
        
        
        # left subtree start = i+1 
        # coz see for the root start was from number not (. thats why i+1 and also end will be before ) and coz in slicing last index is excluded so it works.
        if s[i] == '(':
            lend = self.match_parenth(s,i)
            left_substr = s[i+1: lend]
            
            root.left = self.treeFromString(left_substr)
        
        # right subtree start = lend + 1
        i = lend + 1
        if i < n and s[i] == '(':
            rend = self.match_parenth(s,i)
            right_substr = s[i+1: rend]
            root.right = self.treeFromString(right_substr)
        
        
        return root
            
            
        
            
    def match_parenth(self,s,si):
        count = 0
        for i in range(si,len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            
            if count == 0:
                return i
        
        return -1
        


# ------------------------
def fun2(s):

    if not s:
        return None

    i = 0
    n = len(s)

    while i<n and s[i].isdigit():
        i += 1
    
    root_val = s[:i]
    root = Node(root_val)

    if i >= n:
        return root
    
    elif s[i] == '(':
        j = match_paren(s, i)
        left_str = s[i+1: j]
        root.left = fun2(left_str)
        i = j + 1
    

    if i < n and s[i] =='(' :
        j = match_paren(s,i)
        right_str = s[i+1: j]
        root.right = fun2(right_str)
    
    return root



def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.data, end= " ")
    inorder(root.right)


if __name__ == "__main__":

    # input:
    s = "4(2(3)(1))(6(5))"

    sol = Solution()
    root = sol.treeFromString(s)
    inorder(root)

    # output:
    # 3 2 1 4 5 6 