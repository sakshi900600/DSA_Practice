from collections import Counter
import heapq
class Solution :

    def rearrangeString(self, s):
        #code here
        
        n = len(s)
        freq = Counter(s)
        
        pq = []
        
        for ch, count in freq.items():
            heapq.heappush(pq, (-count,ch))
        
        
        ans = []
        
        # we need to make sure no 2 char are adjacent, 
        # so put the curr char and hold it and 
        # take next char and put in ans and then if the prev still left then
        # push it back to pq
        
        prev_count = 0
        prev_char = ""
        
        while pq:
            count, ch = heapq.heappop(pq)
            ans.append(ch)
            
            if prev_count > 0:
                heapq.heappush(pq, (-prev_count, prev_ch))
            
            
            count = -count
            count -= 1
            
            prev_count, prev_ch = count, ch
            
        
        rear_str = ''.join(ans)
        
        # final check if adjacent char are same or not
        for i in range(1, len(rear_str)):
            if rear_str[i] == rear_str[i-1]:
                return "-1"
        
        
        return rear_str


    def rearrangeString_greedy(self, s):
        #code here
        
        freq = {}
        
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        
        freq_val = freq.values()
        max_freq_val = max(freq_val)
        
        n = len(s)

        # if n % 2 == 0:
        #     if max_freq_val <= n // 2:
        #         return True
        # else:
        #     if max_freq_val <= (n // 2)+1:
        #         return True

        # instead of writing even and odd seperately do this
        if max_freq_val > (n+1)//2:
            return ""
        


                
        
        





if __name__ == '__main__':
    sol = Solution()
    # s = "aaabc" # True
    s = "aaaabc" # False
    print(sol.rearrangeString(s))

    # its incomplete ....