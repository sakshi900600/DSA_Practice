def rearrange(arr):

    pos = []
    neg = []

    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    

    posIdx = 0
    negIdx = 0
    i = 0

    while posIdx < len(pos) and negIdx < len(neg):
        if i%2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        
        i += 1
    
    # rest pos and neg elements
    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1
    
    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1


    return arr



# optimal approach: O(n) time & O(1) space

# logic: We know that at even idx pos/0 should come(c1) & on odd idx neg should come(c2). So while traversing if any one is coming on wrong index we will need to rearrange them. 

# To rearrange :  we find out the first neg/pos from (i+1 --> n) based on condition and then right rotate that part to rearrange. 


class Solution:
    def rearrange1(self,arr):
        # code here
        
        n = len(arr)
        for i in range(n):
            if arr[i]>=0 and i%2==1:
                for j in range(i+1,n):
                    if arr[j] < 0:
                        self.right_rotate(arr,i,j)
                        break
                    
            elif arr[i]<0 and i%2==0:
                for j in range(i+1, n):
                    if arr[j] >= 0:
                        self.right_rotate(arr,i,j)
                        break
    
    
    def right_rotate(self, arr, si,ei):
        # first store the last elem.
        # shift all elem one step forward & at the end put the stored elem on arr[si]
        
        temp = arr[ei]
        
        for i in range(ei,si,-1):
            arr[i] = arr[i-1]
        
        arr[si] = temp
        
        


# input:
arr = [1, 2, 3, -4, -1, 4]

# Output: arr = [1, -4, 2, -1, 3, 4]

print(rearrange(arr))


if __name__ == "__main__":

    sol = Solution()
    arr = [1, 2, 3, -4, -1, 4]

    sol.rearrange1(arr)
    print(arr)

    # Output: [1, -4, 2, -1, 3, 4]

    


    