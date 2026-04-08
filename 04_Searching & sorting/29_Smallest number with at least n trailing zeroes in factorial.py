class Solution:
    def findNum(self, n):
        # code here
        si = 1
        ei = 5*n
        ans = -1
        
        while si <= ei:
            mid = (si+ei)//2
            
            if self.count0(mid) >= n:
                ans = mid
                ei = mid-1
            else:
                si = mid+1
        
        return ans
        
    
    def count0(self, num):
        cnt = 0
        while num > 0:
            num = num//5
            cnt += num
        
        return cnt
    


if __name__ == "__main__":
    sol = Solution()

    n = 6
    print(sol.findNum(n))
    # Output: 25

    