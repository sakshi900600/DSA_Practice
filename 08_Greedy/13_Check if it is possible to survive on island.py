#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        
        total_req = S * M
        sundays = S // 7
        
        # total days shop will open (removed sundays)
        tdso = S - sundays
        
        # maximum we can buy
        max_buy = N * tdso
        
        # check if you can survive
        weekly_req = 7 * M
        weekly_buy_cap = 6 * N
            
        if S >= 7 and (weekly_buy_cap < weekly_req):
            return -1
        elif total_req > max_buy:
            return -1
        
        else:
            if total_req % N == 0:
                min_days = total_req // N
            else:
                min_days = (total_req // N) + 1
            
            return min_days
                
                
                
if __name__ == '__main__':

    # Input: 
    S = 10
    N = 16
    M = 2
    
    # Output: 2
    sol = Solution()
    print(sol.minimumDays(S, N, M))