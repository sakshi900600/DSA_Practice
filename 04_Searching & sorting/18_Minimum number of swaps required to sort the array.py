class Solution:
    # Function to find the minimum number of swaps required to sort the array.

    # correct but tle:
    def minSwaps(self, arr):
        # Code here
        n = len(arr)
        count = 0

        for i in range(n):
            mini = i
            for j in range(i + 1, n):
                if arr[j] < arr[mini]:
                    mini = j

            if mini != i:
                arr[mini], arr[i] = arr[i], arr[mini]
                count += 1

        return count


    def minSwaps_opt(self, arr):
        #Code here
        
        n = len(arr)
        
        pos = {}
        
        for i in range(n):
            pos[arr[i]] = i
        
        arr.sort()
        
        swaps = 0
        vis = [0]*n
        
        for i in range(n):
            if vis[i] == 1 or pos[arr[i]] == i:
                continue
            
            # get cyclesize
            j = i
            cyclesize = 0
            
            while vis[j] == 0:
                vis[j] = 1
                j = pos[arr[j]]
                cyclesize += 1
            
            if cyclesize > 0:
                swaps += cyclesize - 1
        
        return swaps
    




if __name__ == "__main__":
    sol = Solution()

    # input:
    a = [2, 8, 5, 4]

    # print(sol.minSwaps(a))
    print(sol.minSwaps_opt(a))
    # output: 1

