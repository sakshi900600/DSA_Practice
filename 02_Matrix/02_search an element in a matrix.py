class Solution(object):
    def binarySearch(self,arr,target):
        si = 0
        ei = len(arr)-1

        while si <= ei:
            mid = (si+ei)//2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                si = mid+1
            else:
                ei = mid-1
        
        return False


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if target >= matrix[i][0] and target <= matrix[i][m-1]:
                return self.binarySearch(matrix[i],target)
        
        return False



    # 2nd approach: Assuming the 2D matrix as a 1D list:
    def searchMatrix2(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])


        # 2nd approach:
        # by assuming 2D matrix as a 1D list and then applying binary search
        # and for row and col number using this:

        # row no = mid / m
        # col no = mid % m

        si = 0
        ei = (n*m)-1

        while si <= ei:
            mid = (si+ei)//2
            row_no = mid // m
            col_no = mid % m

            if matrix[row_no][col_no] == target:
                return True

            elif matrix[row_no][col_no] < target:
                si = mid+1
            else:
                ei = mid-1
        

        return False



 

if __name__ == "__main__":
    sol = Solution()

    # Input: 
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    # Output: true

    # print(sol.searchMatrix(matrix,target))
    print(sol.searchMatrix2(matrix,target))