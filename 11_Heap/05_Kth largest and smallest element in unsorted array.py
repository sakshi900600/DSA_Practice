import heapq

class Solution:
    def kLargest(self, arr, k):
        min_heap = []
        for num in arr:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return sorted(min_heap, reverse=True)


    def kSmallest(self, arr, k):
        min_heap = []

        for i in range(len(arr)):
            heapq.heappush(min_heap, -arr[i])

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        ans = []
        for i in range(k):
            ans.append(-heapq.heappop(min_heap))
            
        return sorted(ans)





if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    sol = Solution()
    print(sol.kLargest(arr, k))  # Output: [6, 5]
    print(sol.kSmallest(arr,k)) # Output: [1,2]

