# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2026-05-06

# not complete...

class Solution(object):

    def reverse(self, arr):
        si = 0
        ei = len(arr)-1

        while si <= ei:
            arr[si],arr[ei] = arr[ei],arr[si]
            si += 1
            ei -= 1

        

    def rotateTheBox(self, mat):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(mat)
        m = len(mat[0])
        rom = [[] for _ in range(m)]

        # rotate matrix
        for i in range(n):
            for j in range(m):
                rom[j].append(mat[i][j])
        
        # print(rom)
        for r in range(m):
            self.reverse(rom[r])
        
        # print(rom)

        # change positions
        for c in range(n):
            for r in range(m-1,-1,-1):
                if rom[r][c] == '.':

                    isobs = False
                    x = r-1
                    while x>=0 and rom[x][c] != '#':
                        if rom[x][c] == '*':
                            isobs = True
                            break
                        x -= 1

                    if isobs == False:
                        rom[r][c] = '#'
                        rom[x][c] = '.'

        return rom
        



if __name__ == "__main__":

    sol = Solution()
    mat = [["#",".","*","."],
        ["#","#","*","."]]
    
    print(sol.rotateTheBox(mat))