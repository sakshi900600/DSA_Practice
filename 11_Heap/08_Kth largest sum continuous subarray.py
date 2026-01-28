from typing import List

import heapq
class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        n = len(arr)
        
        # using list + sorting
        # li = []
        # for i in range(n):
        #     for j in range(i,n):
        #         subarr_sum = sum(arr[i:j+1])
        #         li.append(subarr_sum)
        
        # li.sort(reverse = True)
        # # print(li)
        # return li[k-1]
        
        
        # using priotiy q
        # pq = []
        # for i in range(n):
        #     for j in range(i,n):
        #         subarr_sum = sum(arr[i:j+1])
        #         heapq.heappush(pq, -subarr_sum)
                
        
        # kth_max = float('-inf')
        # for i in range(k):
        #     kth_max = heapq.heappop(pq)
                
        # return -kth_max
                
                
        
        # using priority q by fixing k size
        pq = []
        for i in range(n):
            curr_sum = 0
            for j in range(i,n):
                curr_sum += arr[j]
                
                if len(pq) < k:
                    heapq.heappush(pq, curr_sum)
                else:
                    if curr_sum > pq[0]:
                        heapq.heappop(pq)
                        heapq.heappush(pq, curr_sum)
        
        
        return pq[0]
                
                
                       
if __name__ == "__main__":
    arr = [3,2,1]
    k = 2
    sol = Solution()
    print(sol.kthLargest(arr, k))
    # Output: 5

