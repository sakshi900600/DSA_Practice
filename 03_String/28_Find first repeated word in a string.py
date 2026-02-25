#User function Template for python3

class Solution:

    def firstRepeated(self, arr,n):
        dct = {}

        for elem in arr:
            dct[elem] = dct.get(elem,0)+1
        
        for elem in arr:
            if dct[elem] > 1:
                return elem
            
        return -1


    def secFrequent(self, arr, n):
        # code here
        
        dct = {}
        
        for word in arr:
            dct[word] = dct.get(word,0)+1
        
        sorted_val = sorted(dct.values(), reverse=True)
        # print(sorted_val)
        
        req_freq = sorted_val[1]
        
        for k,v in dct.items():
            if v == req_freq:
                return k
        
        return -1
    


if __name__ == "__main__":
    sol = Solution()

    arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
    n = len(arr)

    print(sol.firstRepeated(arr,n))
    print(sol.secFrequent(arr,n))

    # Output: aaa, bbb
    