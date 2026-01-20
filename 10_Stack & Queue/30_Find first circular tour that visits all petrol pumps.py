# I didn't understand the solution. 

# My doubt:
# suppose there exists 2 valid start indices, but the first one is not valid for the entire tour, but in this code while finding valid possible starts, it will return first one and in validity check it will fail so directly return -1 but second one will be correct then it can be wrong. 


class Solution:
    def startStation(self, gas, cost):
        #  code here
        
        n = len(gas)
        
        startIdx = 0
        curr_gas = 0
        
        # find valid possible starts
        for i in range(n):
            curr_gas = curr_gas + gas[i] - cost[i]
            
            if curr_gas < 0:
                startIdx = i + 1
                curr_gas = 0
        
        
        # now check validity of startIndex
        curr_gas = 0
        for i in range(n):
            idx = (i+startIdx) % n # circlar index 
            curr_gas = curr_gas + gas[idx] - cost[idx]
            
            if curr_gas < 0:
                return -1
                
        
        return startIdx
        
              


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    result = solution.startStation(gas, cost)
    print(result)  # Output: 3