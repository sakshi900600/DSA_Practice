#User function Template for python3

class Solution:
    def pageFaults(self, N, C, pages):
        # code here
        
        count = 0
        memory = []
        
        for i in range(N):
            if pages[i] not in memory:
                
                if len(memory) == C:
                    memory.pop(0)
                
                memory.append(pages[i])
                count += 1
            else:
                memory.remove(pages[i])
                memory.append(pages[i])
        
        
        return count



if __name__ == '__main__':
    sol = Solution()
    N = 9
    C = 4
    pages = [5, 0, 1, 3, 2, 4, 1, 0, 5]

    # Output: 8
    print(sol.pageFaults(N, C, pages))