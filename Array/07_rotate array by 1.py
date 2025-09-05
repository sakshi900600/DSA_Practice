
# using extra space approach - gives tle.
def rotateby1(arr):
    n = len(arr)

    ans = []
    k = 1

    for i in range(n):
        idx = (i+k)%n
        ans.insert(idx, arr[i])
    
    return ans



def rotatebyOne(arr):
    n = len(arr)
    k = 1
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)


def reverse(arr,si,ei):
    while si <= ei:
        temp = arr[si]
        arr[si] = arr[ei]
        arr[ei] = temp
        si += 1
        ei -= 1





# final solution:  ----------------------------------------

class Solution:
    def reverse(self,arr, si,ei):
        while si <= ei:
            temp = arr[si]
            arr[si] = arr[ei]
            arr[ei] = temp
            
            si += 1
            ei -= 1
            
            
    def rotate(self, arr):
        
        n = len(arr)
        k = 1
        # its universal code you can rotate arr with any index value.
        self.reverse(arr,0,n-1)
        self.reverse(arr,0,k-1)
        self.reverse(arr,k,n-1)
        
    

if __name__ == '__main__':

    sol = Solution()


    # input:
    a = [1,2,3,4,5]

    # output:
    # [5, 1, 2, 3, 4]

    
    # print(rotateby1(a))
    sol.rotate(a)
    print(a)