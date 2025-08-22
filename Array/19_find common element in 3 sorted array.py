#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        
        s1 = set(arr1)
        s2 = set(arr2)
        s3 = set(arr3)
        
        s = s1.intersection(s2)
        
        ans_set = s.intersection(s3)
        
        ans = list(ans_set)
        
        ans.sort()
        
        
        return ans
    


if __name__ == '__main__':
    sol = Solution()

    # input:
    arr1 = [1, 5, 10, 20, 40, 80] 
    arr2 = [6, 7, 20, 80, 100] 
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    # Output: [20, 80]
    print(sol.commonElements(arr1,arr2,arr3))
