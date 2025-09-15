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
    
    # common elem using sorted array property
    def common_elem(self,a1,a2,a3):
        i =0
        j =0
        k =0
        ans = []

        while i<len(a1) and j<len(a2) and k<len(a3):
            if a1[i] == a2[j] == a3[k]:
                ans.append(a1[i])
                i+= 1
                j+= 1
                k += 1
            elif a1[i]<a2[j] and a1[i]<a3[k]:
                i += 1
            elif a2[j]<a1[i] and a2[j]<a3[k]:
                j += 1
            else:
                k += 1

        return ans
        


if __name__ == '__main__':
    sol = Solution()

    # input:
    arr1 = [1, 5, 10, 20, 40, 80] 
    arr2 = [6, 7, 20, 80, 100] 
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    # Output: [20, 80]
    # print(sol.commonElements(arr1,arr2,arr3))
    print(sol.common_elem(arr1,arr2,arr3))

