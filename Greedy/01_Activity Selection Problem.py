#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        
        # create meetings
        meetings = []
        for i in range(len(start)):
            meet = (start[i], end[i])
            meetings.append(meet)
        
        # sort meetings based on ending
        meetings.sort(key= lambda x: x[1])
        
        ans = []
        ans.append(meetings[0])
        count = 1
        
        for meet in meetings:
            curr_meet = meet
            last_meet = ans[-1]
            
            if curr_meet[0] > last_meet[1]:
                ans.append(curr_meet)
                count += 1
        
        
        return count
        
        

if __name__ == "__main__":
    # Input: 
    start = [1, 3, 0, 5, 8, 5]
    end =  [2, 4, 6, 7, 9, 9]
    # Output: 4

    sol = Solution()
    print(sol.maximumMeetings(start, end))
