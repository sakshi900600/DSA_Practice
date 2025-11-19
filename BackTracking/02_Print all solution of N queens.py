class Solution:
    def nQueen(self, n):

        mat = [[''] * n for _ in range(n)]
        solns = []

        def placeQueen(row, mat, curr):
            if row == n:
                solns.append(curr[:])# store copy of curr       
                return

            for col in range(n):
                if self.isSafe(row, col, mat):
                    mat[row][col] = 'q'
                    curr.append(col + 1)    
                    placeQueen(row + 1, mat, curr)
                    
                    # BACKTRACK
                    curr.pop()
                    mat[row][col] = ''


        placeQueen(0, mat, [])
        return solns

    def isSafe(self, row, col, mat):
        n = len(mat)
        
        # check column upwards
        r = row - 1
        while r >= 0:
            if mat[r][col] == 'q':
                return False
            r -= 1

        # upper left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if mat[r][c] == 'q':
                return False
            r -= 1
            c -= 1

        # upper right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if mat[r][c] == 'q':
                return False
            r -= 1
            c += 1

        return True



if __name__ == "__main__":
    sol = Solution()

    n = 4
    print(sol.nQueen(n))

    # Output: [[2, 4, 1, 3], [3, 1, 4, 2]]