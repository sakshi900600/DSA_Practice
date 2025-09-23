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
    def findTripletWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        
        tail = head
        while tail.next != None:
            tail = tail.next
            
        ans = []
        
        temp = head
        while temp.next != None and temp.next.next != None: # or we can check temp.next != None
            left = temp.next
            right = tail
        
            while left != None and right != None and left != right and left.prev != right:
                sum = temp.data + left.data + right.data
                
                if sum == target:
                    ans.append((temp.data, left.data, right.data))
                    left = left.next
                    right = right.prev
                elif sum < target:
                    left = left.next
                else:
                    right = right.prev
            

            temp = temp.next
                
        
        return ans
        
        