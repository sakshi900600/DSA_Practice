class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        ans = []
        n = len(intervals)

        # sort intervals:
        intervals.sort()

        ans.append(intervals[0])

        for i in range(n):
            curr_interval = intervals[i]
            last_interval = ans[-1]

            if curr_interval[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], curr_interval[1])
            else:
                ans.append(curr_interval)
        

        return ans
        


if __name__ == '__main__':

    sol = Solution()

    # input:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # output:
    # [[1,6],[8,10],[15,18]]

    print(sol.merge(intervals))