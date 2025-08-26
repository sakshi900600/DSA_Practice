# works but tle 🤪

def subset():
    a = [1,2,2]
    b = [1,1]

    for i in b:
        if i not in a:
            return False
        else:
            a.remove(i)
        
    return True


# print(subset())


#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a.sort()
        b.sort()
        
        i=0
        j=0
        
        while i<len(a) and j<len(b):
            if a[i] < b[j]:
                # if less that than can be found later
                i += 1
            elif a[i] == b[j]:
                i += 1
                j += 1
            else:
                # if b elem become lesser than a,
                # that means not no a
                return False
                
        
        # if all elem of b is traversed
        return j == len(b)
    
    


# output:
if __name__ == "__main__":
    sol = Solution()

    # input:   
    a = [1,2,2]
    b = [1,1]
    # Output: False

    print(sol.isSubset(a,b))