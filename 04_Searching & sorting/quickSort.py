# quick sort:
# In quick sort we choose last elem as pivot and then we put less elem then pivot on left side and greater on right side and in each pass we fix one elem (pivot) at its correct position.
# But the left and right parts are internally unsorted. so we did recursive calls for (low, pivot-1) and (pivot+1, high) .

# in partition fun after moving greater elem than pivot, we fix the pivot position by swapping ith value with arr[high]. 

# If we simply swap pivot with arr[i] then it will just swap 2 var the pivot will point to arr[high], but if one elem is fixed then pivot should move. 


class Solution:
    def quickSort(self, arr, low, high):
        #code here 
        if low >= high:
            return
        
        pidx = self.partition(arr,low,high)
        self.quickSort(arr, low, pidx-1)
        self.quickSort(arr, pidx+1, high)
        
        

    def partition(self, arr, low, high):
        #code here
        pivot = arr[high]
        i = low-1
        
        for j in range(low,high):
            if arr[j] <= pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j] #swap
            
        
        # put pivot on its correct idx 
        i += 1
        arr[high], arr[i] = arr[i], arr[high]
        
        return i # new pivot idx
        
        

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    ob = Solution()
    ob.quickSort(arr, 0, n-1)
    print("Sorted array is:", arr)
        
