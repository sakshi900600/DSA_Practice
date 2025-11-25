class Solution:
    def medianOf2(self, a, b):
        # code here
        
        li = []
        
        for it in a:
            li.append(it)
            
        for it in b:
            li.append(it)
                
                
        li.sort()
                
        if len(li) % 2 != 0:
            return li[len(li)//2]
        else:
            e1 = li[len(li)//2]
            e2 = li[(len(li)//2) - 1]
            
            return (e1+e2)/2
            

if __name__ == "__main__":
    sol = Solution()

    # input:
    a = [3, 5, 6, 12, 15]
    b = [3, 4, 6, 10, 10, 12]
    # Output: 6

    print(sol.medianOf2(a,b))
