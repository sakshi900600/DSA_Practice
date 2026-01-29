import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        
        if max(freq.values()) > (n+1)//2:
            return ""

        max_heap = []
        for char,count in freq.items():
            heapq.heappush(max_heap, (-count, char))

        ans = []
        while len(max_heap) >= 2:
            count1, ch1 = heapq.heappop(max_heap)
            count2, ch2 = heapq.heappop(max_heap)

            ans.append(ch1)
            ans.append(ch2)

            count1 = -count1 - 1
            count2 = -count2 - 1

            if count1 > 0:
                heapq.heappush(max_heap, (-count1, ch1))

            if count2 > 0:
                heapq.heappush(max_heap, (-count2, ch2))
            
        
        if max_heap:
            count, ch = heapq.heappop(max_heap)
            if count > 1:
                return ""
            ans.append(ch)
        
        return "".join(ans)
            


if __name__ == "__main__":
    sol = Solution()

    s = "aab"
    print(sol.reorganizeString(s))






        