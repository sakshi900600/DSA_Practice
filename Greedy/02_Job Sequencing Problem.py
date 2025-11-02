class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        
        maxProfit = 0
        count = 0
        
        # create jobs pair
        jobs = []
        for i in range(len(profit)):
            j = deadline[i]
            p = profit[i]
            
            newJob = (j,p)
            jobs.append(newJob)
            
        
        # find max deadline so that we can add jobs in slots.
        max_deadline = max(deadline)
        
        # i am creating +1 extra size but i will never use 0th index. its just to sync deadline and index value.
        arr = [0]*(max_deadline+1)
        
        # sort job based on profit
        jobs.sort(key=lambda x: x[1], reverse="True")
        
        
        for job in jobs:
            d = job[0]
            p = job[1]
            
            # checking free slot from backward
            for i in range(d, 0, -1):
                if arr[i] == 0:
                    arr[i] = 1
                    count += 1
                    maxProfit += p
                    break
                
        
        return [count, maxProfit]
        
        

if __name__ == "__main__":
    # input:
    deadline = [2, 1, 2, 1, 3]
    profit = [100, 19, 27, 25, 15]
    
    # output: [3 142]
    obj = Solution()
    print(obj.jobSequencing(deadline, profit))