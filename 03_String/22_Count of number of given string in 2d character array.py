# only for 4 directions: top-down, down-top, left-right, right-left
#User function Template for python3

class Solution:
    def findOccurrence(self,mat,target):
        n = len(mat)
        m = len(mat[0])
        
        count = 0
        
        for i in range(n):
            txt = "".join(mat[i])
            count += self.rabinKarp(target,txt)
            count += self.rabinKarp(target,txt[::-1])
        
        for j in range(m):
            txt = "".join(mat[i][j] for i in range(n))
            count += self.rabinKarp(target,txt)
            count += self.rabinKarp(target,txt[::-1])
        
        return count 
    

    def rabinKarp(self, pat, txt):
        n = len(txt)
        m = len(pat)
        
        if m > n or m == 0:
            return 0
        
        base = 256
        mod = 101
        
        h = 1
        pat_hash = 0
        wndo_hash = 0
        
        # h = base^(m-1)
        for i in range(m-1):
            h = (h * base) % mod
        
        # initial hash values
        for i in range(m):
            pat_hash = (pat_hash * base + ord(pat[i])) % mod
            wndo_hash = (wndo_hash * base + ord(txt[i])) % mod
        
        count = 0
        for i in range(n - m + 1):
            if wndo_hash == pat_hash:
                if pat == txt[i:i+m]:
                    count += 1
            
            # Update hash for next window (if there is a next window)
            if i < n - m:
                # Remove leftmost character
                wndo_hash = (wndo_hash - ord(txt[i]) * h) % mod
                # Add new rightmost character
                wndo_hash = (wndo_hash * base + ord(txt[i + m])) % mod
                if wndo_hash < 0:
                    wndo_hash += mod
        
        return count
    


# Find the number of occurrences of a given search word in a 2d-Array of characters where the word can go up, down, left, right, and around 90-degree bends.
# Note: While making a word you can use one cell only once.

class Solution2:
    def findOccurrence(self, mat, target):
        n = len(mat)
        m = len(mat[0])
        
        word = target
        count = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    vis = [[False]*m for _ in range(n)]
                    count += self.dfs(i, j, 0, mat, word, vis)
        
        return count
    
    
    def dfs(self, r, c, idx, mat, word, vis):
        # Check if current cell matches
        if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]):
            return 0
            
        if vis[r][c]:
            return 0
            
        if mat[r][c] != word[idx]:
            return 0
        
        # If this is the last character, found one path
        if idx == len(word) - 1:
            return 1
        
        # Mark current cell
        vis[r][c] = True
        
        # Try all 4 directions
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total = 0
        
        for dr, dc in moves:
            nr = r + dr
            nc = c + dc
            total += self.dfs(nr, nc, idx + 1, mat, word, vis)
        
        # Backtrack
        vis[r][c] = False
        
        return total
        
        


if __name__ == "__main__":

    sol = Solution()
    target = "MAGIC"
    mat = ["BBABBM", "CBMBBA", "IBABBG", "GOZBBI", "ABBBBC", "MCIGAM"]
    print(sol.findOccurrence(mat,target))
    # Output: 3
    
    sol2 = Solution2()
    mat2 = [['c','a','t'],['a','t','c'],['c','t','a']]
    target = "cat"
    print(sol2.findOccurrence(mat2,target))

    # Output:5

