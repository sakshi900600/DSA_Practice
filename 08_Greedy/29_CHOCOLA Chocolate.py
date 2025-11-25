class Solution:
    def minCost(self, n, m, x, y):
        # code here
        
        x.sort(reverse='True')
        y.sort(reverse='True')
        
        i = 0
        j = 0
        
        vs = 1  # vertical segment count
        hs = 1  # horizontal segment count
        
        total_cost = 0
        
        while i < len(x) and j < len(y):
            # vertical cut
            if x[i] >= y[j]:
                total_cost += x[i] * hs
                vs += 1
                i += 1
            else:  # horizontal cut
                total_cost += y[j] * vs
                hs += 1
                j += 1
        
        
        # for leftover
        while i < len(x):
            total_cost += x[i] * hs
            vs += 1
            i += 1
        
        while j < len(y):
            total_cost += y[j] * vs
            hs += 1
            j += 1
        
        return total_cost
        
        

if __name__ == "__main__":
    n = 6
    m = 4
    x = [2, 1, 3, 1, 4]
    y = [4, 1, 2]
    
    sol = Solution()

    # Output: 42
    print(sol.minCost(n, m, x, y))  