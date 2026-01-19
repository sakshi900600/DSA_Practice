class Solution:
    def startStation(self, gas, cost):
        #  code here
        
        n = len(gas)
        
        for i in range(n):
            if gas[i] > cost[i]:
                idx = i
                total_gas = 0
                
                while idx != i:
                    if idx == n:
                        idx = 0
                    
                    total_gas += gas[i]
                    total_gas -= cost[i]
                    
                    if total_gas <= 0:
                        break
                    
                    idx += 1
                    
                return i
        
        return -1
        
        


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    result = solution.startStation(gas, cost)
    print(result)  # Output: 3