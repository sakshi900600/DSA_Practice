class Solution:

    # with extra space
    def majorityElement(self, arr):
        #code here
        n = len(arr)
        dct = {}
        
        for i in arr:
            dct[i] = dct.get(i,0)+1
            
        
        ans = -1
        for k,v in dct.items():
            if v > n/2:
                ans = k
                break
                
                
        return ans
                

    # without extra space
    def majority_elem(self,arr):
        count = 0
        elem = -1

        # finding elem which can be a majority elem
        for i in arr:
            if count == 0:
                elem = i
                count = 1
            elif i == elem:
                count += 1
            else:
                count -= 1
        

        # final check
        count = 0
        for num in arr:
            if num == elem:
                count += 1
        
        if count > len(arr)/2:
            return elem
        
        return -1


if __name__ == "__main__":
    sol = Solution()

    # input
    arr = [1, 1, 2, 1, 3, 5, 1]
    # Output: 1

    print(sol.majority_elem(arr))
    print(sol.majorityElement(arr))