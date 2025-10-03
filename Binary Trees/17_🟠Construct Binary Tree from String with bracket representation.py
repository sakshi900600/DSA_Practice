from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

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
        
