from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        
        meets = []
        for i in range(N):
            start = S[i]
            end = F[i]
            mid = i + 1
            
            meets.append((mid,start,end))
        
        meets.sort(key=lambda x: x[2])
        
        
        ans = []
        ans.append(meets[0])
        
        meet_ids = []
        meet_ids.append(meets[0][0])
        
        
        for meet in meets[1:]:
            last_meet = ans[-1]
            curr_meet = meet
            
            if last_meet[2] < curr_meet[1]:
                ans.append(curr_meet)
                meet_ids.append(curr_meet[0])
        
        
        meet_ids.sort()
        return meet_ids
                
            
        
if __name__ == "__main__":
    sol = Solution()
    
    N = 6
    S = [1, 3, 0, 5, 8, 5]
    F = [2, 4, 6, 7, 9, 9]

    # Output: [1, 2, 4, 5]
    print(sol.maxMeetings(N, S, F))  
