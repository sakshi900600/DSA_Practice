#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        bitarr = [[] for _ in range(32)]
        
        for i in range(n):
            setbitcnt = self.countSetBit(arr[i])
            bitarr[setbitcnt].append(arr[i])
        
        j = 0
        for i in range(31, -1, -1):
            # traverse in inner list
            for elem in bitarr[i]:
                arr[j] = elem
                j += 1
        
        return arr
        
        
    def countSetBit(self, num):
        count = 0
        
        while num:
            if num % 2 != 0:
                count += 1
            
            num = num //2
        
        return count
        
    # using builtin fun
    def sortBySetBitCount_f(self, arr,n):
        arr.sort(key= lambda x: bin(x).count('1'), reverse=True)
        return arr
    
    


if __name__ == "__main__":
    sol = Solution()

    arr = [1, 2, 3, 4, 5, 6]
    print(sol.sortBySetBitCount(arr, len(arr)))
    print(sol.sortBySetBitCount_f(arr, len(arr)))

    # Output: [3, 5, 6, 1, 2, 4]
