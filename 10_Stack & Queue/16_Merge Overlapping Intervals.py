class Solution():


    def mergeOverlap(self, arr):
        n = len(arr)
        arr.sort()

        ans = [] # stack
        ans.append(arr[0])

        for i in range(1,n):
            curr = arr[i]
            last = ans[-1]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                ans.append(curr)

        return ans


    


if __name__ == "__main__":
    sol = Solution()

    arr = [[1,3],[2,4],[6,8],[9,10]]
    # Output: [[1, 4], [6, 8], [9, 10]]

    print(sol.mergeOverlap(arr))