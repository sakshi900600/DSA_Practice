class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def getKthNode(head, k):
    temp = head
    k -= 1

    while k >0 and temp != None:
        temp = temp.next
        k -= 1
    
    return temp


def reverse(head):
    if head == None or head.next == None:
        return head

    curr =  head
    prev = None

    while curr != None:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    
    return prev


def rotate_dll(head, k):
    if head == None or head.next == None or k==1:
        return head
    
    temp = head
    prev_node = None

    while temp != None:
        kth_node = getKthNode(temp, k)

        if kth_node == None:
            if prev_node == None:
                return head
            else:
                prev_node.next = temp
                temp.prev = prev_node
                return head
        

        next_node = kth_node.next
        kth_node.next = None
        next_node.prev = None

        reverse(temp)

        if temp == head:
            head = kth_node
        
        if prev_node == None:
            prev_node = temp
        else:
            prev_node.next = kth_node
            kth_node.prev = prev_node
            prev_node = temp
        
        temp = next_node

    return head





if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head

    head.next.next = Node(3)
    head.next.next.prev = head.next

    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    head.next.next.next.next = Node(5)
    head.next.next.next.next.prev = head.next.next.next

    k = 3
    new_head = rotate_dll(head, k)
    temp = new_head

    while temp != None:
        print(temp.data, end=" <-> ")
        temp = temp.next
    



