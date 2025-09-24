'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        # code here
        li = []
        
        for ll in arr:
            head = ll
            
            while head != None:
                li.append(head.data)
                head = head.next
        
        
        # print(li)
        li.sort()
        dummy = Node(-1)
        temp = dummy
        
        for data in li:
            newNode = Node(data)
            temp.next = newNode
            temp = newNode
        
        return dummy.next
        
            
            
            
            
            
            