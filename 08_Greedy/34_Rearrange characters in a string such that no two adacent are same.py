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
                return ""
        
        
        return rear_str


    # My approach --------------
    def rearrange_String(self, s):
        #code here
        n = len(s)
        
        freq = {}
        maxfcnt = 0
        maxfch = '#'
        
        for ch in s:
            freq[ch] = freq.get(ch, 0)+1
            
            if freq[ch] > maxfcnt:
                maxfcnt = freq[ch]
                maxfch = ch
        
        
        # checking possiblity
        if maxfcnt > ((n+1)//2):
            return ""
            
        # put max freq char at even index
        slist = list(s)
        idx = 0
        
        while maxfcnt > 0:
            slist[idx] = maxfch
            idx += 2
            maxfcnt -= 1
        
        # mark max freq char freq as 0.
        freq[maxfch] = 0
        
        # put rest char at even or odd index
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            while freq.get(ch,0) > 0:
                if idx >= n:
                    idx = 1
                
                slist[idx] = ch
                idx += 2
                freq[ch] -= 1
        
        
        return "".join(slist)
        
        



if __name__ == '__main__':
    sol = Solution()
    # s = "aaabc" # abaca
    s = "aaaabc" # ""
    print(sol.rearrange_String(s))

