import heapq
class Solution:    
    
    # My very own approach 💖🥳 - TLE
    def minPlatform(self, arr, dep):
        # code here
        
        trains = []
        
        for i in range(len(arr)):
            trains.append((arr[i], dep[i]))
            
        trains.sort()
        
        dct = {}
        dct[0] = trains[0][1]
        
        count = 1
        
        for train in trains[1:]:
            a = train[0]
            d = train[1]
            
            val = self.helper(dct, a)
            
            if val != -1:
                dct[val] = d
            else:
                dct[count] = d
                count += 1
                
        return count
        
        
    def helper(self, dct, a):
        
        for k,v in dct.items():
            if a > v:
                return k
        return -1



    # lets optimize it    
    # we are trying to find out arrival time >dept value  stored in dct.
    # carefully observe we always find out smallest dept value.
    # And we can get smallest value in o(1) using min-heap.

    def minPlatform_opt(self, arr, dep):
        # code here
        
        trains = []
        
        for i in range(len(arr)):
            trains.append((arr[i], dep[i]))
            
        trains.sort()
        
        pq = []
        heapq.heappush(pq, trains[0][1])
        
        count = 1
        
        for train in trains[1:]:
            a = train[0]
            d = train[1]
            
            # if curr arrival > last min dept time
            if pq and a > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, d)
            else:
                count += 1
                heapq.heappush(pq, d)
            
        return count



if __name__ == "__main__":
    sol = Solution()
    # input:
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    # Output: 3
    print(sol.minPlatform(arr, dep))  
    print(sol.minPlatform_opt(arr, dep))  
        