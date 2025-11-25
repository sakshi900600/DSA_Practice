class Solution:
    def mergeArrays(self, a, b):
        # code here
        
        n = len(a)
        m = len(b)
        
        i = n-1
        j = 0
        
        while i>=0 and j<m:
            if a[i] > b[j]:
                a[i],b[j] = b[j],a[i]
            
            i -= 1
            j += 1
        
        
        a.sort()
        b.sort()
        


if __name__ == '__main__':

    sol = Solution()

    # input:
    a = [2, 4, 7, 10]
    b = [2, 3]

    # output: 
    # a = [2, 2, 3, 4], b = [7, 10]
    
    sol.mergeArrays(a,b)
    print(a)
    print(b)