class Solution:
    def kthElement(self, a, b, k):
        # code here
        
        li = []
        
        for i in a:
            li.append(i)
            
        for j in b:
            li.append(j)
            
        li.sort()
        
        return li[k-1]
        


if __name__ == "__main__":
    sol = Solution()

    # input:
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5

    # Output: 6
    
    print(sol.kthElement(a,b,k))