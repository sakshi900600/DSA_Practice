import heapq

class Solution:
    def minValue(self, s, k):
        #code here
        
        freq = {}
        pq = []
        
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
            
        
        for v in freq.values():
            heapq.heappush(pq, -v)
        
        # print(pq)
        
        while pq and k>0:
            top = heapq.heappop(pq)
            top = -top-1
            k -= 1
            
            if top > 0:
                heapq.heappush(pq, -top)
        
        # print(pq) 
        sum = 0
        while pq:
            top = heapq.heappop(pq)
            sum += (top*top)
        
        return sum
            
            
        
        
if __name__ == "__main__":   
    s = "aaab"
    k = 2
    sol = Solution()
    print(sol.minValue(s, k))
    # Output: 2