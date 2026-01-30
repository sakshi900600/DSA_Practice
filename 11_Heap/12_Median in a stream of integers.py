import heapq
class Solution:

    # tle ------
    def getMedian(self, arr):
        # code here
        n = len(arr)
        ans = []
        
        i = 0
        for j in range(n):
            subarr = sorted(arr[i:j+1])
            med = self.median(subarr)
            ans.append(med)
        
        return ans
        
    
    def median(self, arr):
        n = len(arr)
        
        if n%2 != 0:
            return arr[n//2]
        else:
            e1 = arr[n//2]
            e2 = arr[(n//2)-1]
            return (e1+e2)/2


    # Optimized using heap
    def getMedian(self, arr):
        # code here
        n = len(arr)
        ans = []
        
        left_max_heap = []
        right_min_heap = []
        
        for i in range(n):
            heapq.heappush(left_max_heap, -arr[i])
            
            # pop largest elem from lmh and put in rmh to maintain sorted order
            max_val = -heapq.heappop(left_max_heap)
            heapq.heappush(right_min_heap, max_val)
            
            # balance elems in both heaps
            if len(right_min_heap) > len(left_max_heap):
                elem = heapq.heappop(right_min_heap)
                heapq.heappush(left_max_heap, -elem)
            
            # calculate median
            if len(left_max_heap) != len(right_min_heap):
                ans.append(-left_max_heap[0])
            else:
                ans.append((-left_max_heap[0] + right_min_heap[0])/2.0)
                
                
        return ans



if __name__ == "__main__":
    sol = Solution()
    
    arr = [5, 15, 1, 3,2,8]
    print(sol.getMedian(arr))

    # Output: [5, 10.0, 5, 4.0, 3, 4.0]

            
        