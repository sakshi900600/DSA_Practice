# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        mod = 1000000007
        
        num1 = 0
        num2 = 0
        
        temp1 = first
        temp2 = second
        
        while temp1 != None:
            num1 = (num1*10 + temp1.data) % mod
            temp1 = temp1.next
        
        while temp2 != None:
            num2 = (num2*10 + temp2.data) % mod
            temp2 = temp2.next
            
            
        return (num1 * num2) % mod    
            



if __name__ == "__main__":
    first = Node(1)
    first.next = Node(0)
    first.next.next = Node(0)

    second = Node(1)
    second.next = Node(0)

    sol = Solution()
    result = sol.multiply_two_lists(first, second)
    print(result)  
    # Output = 1000