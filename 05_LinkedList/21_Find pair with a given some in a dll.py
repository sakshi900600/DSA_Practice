from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        
        tail = head
        while tail.next != None:
            tail = tail.next
            
        ans = []
        
        left = head
        right = tail
        
        while left.data < right.data:
            sum = left.data + right.data
            
            if sum == target:
                ans.append((left.data, right.data))
                left = left.next
                right = right.prev
            elif sum < target:
                left = left.next
            else:
                right = right.prev
                
        
        return ans
        
        