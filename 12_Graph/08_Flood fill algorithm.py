class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        initial_col = image[sr][sc]
        if color == initial_col:
            return image
            
        self.dfs(initial_col, color, sr,sc,image)

        return image


    
    def dfs(self, initial_col, color, sr,sc, image):
        image[sr][sc] = color

        adj = [(1,0), (0,-1), (0,1), (-1,0)]

        for x in range(4):
            nr = sr + adj[x][0]
            nc = sc + adj[x][1]

            if self.isSafe(nr,nc,image) and image[nr][nc] == initial_col:
                self.dfs(initial_col, color, nr,nc,image)
    

    def isSafe(self, r,c,image):
        n = len(image)
        m = len(image[0])

        c1 = 0 <= r < n
        c2 = 0 <= c < m

        return c1 and c2


if __name__ == "__main__":
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(sol.floodFill(image, sr, sc, color))
    # Output: [[2,2,2],[2,2,0],[2,0,1]]


    