class Solution:
    def inversionCount(self, arr):
        # Code Here
        return self.merge_sort_count(arr,0,len(arr)-1)
    
    def merge_sort_count(self,arr,si,ei):
        if si >= ei:
            return 0
        
        mid = (si+ei)//2
        
        inversion = 0
        
        inversion += self.merge_sort_count(arr,si,mid)
        inversion += self.merge_sort_count(arr,mid+1,ei)
        
        inversion += self.merge(arr,si,mid,ei)
        
        return inversion
    
    
    def merge(self,arr,si,mid,ei):
        i = si
        j = mid+1
        temp = []
        inversion = 0
        
        while i<=mid and j<=ei:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inversion += (mid-i+1)
                j += 1
                
        while i<=mid:
            temp.append(arr[i])
            i += 1
        
        while j<=ei:
            temp.append(arr[j])
            j += 1
        
        
        for k in range(si,ei+1):
            arr[k] = temp[k-si]
            
            
        return inversion
            
            
            
# using modified merge sort logic.  

def count_inversions(arr):
    return merge_sort_count(arr,0,len(arr)-1)


def merge_sort_count(arr,si,ei):
    if si >= ei:
        return 0
    
    mid = (si+ei)//2
    inversion = 0

    inversion += merge_sort_count(arr,si,mid)
    inversion += merge_sort_count(arr,mid+1,ei)

    inversion += merge(arr,si,mid,ei)

    return inversion


def merge(arr,si,mid,ei):
    i = si
    j = mid+1
    temp = []
    inversion = 0

    while i<= mid and j <= ei:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inversion += (mid-i+1) # inversion count
            j += 1
    
    while i<= mid:
        temp.append(arr[i])
        i += 1

    while j <= ei:
        temp.append(arr[j])
        j += 1
    

    for k in range(si,ei+1):
        arr[k] = temp[k-si]
    

    return inversion



# input:
arr = [2, 4, 1, 3, 5]
# Output: 3
print(count_inversions(arr))