class Solution:
    # Function to find the minimum number of swaps required to sort the array.

    # correct but tle:
    def minSwaps(self, arr):
        # Code here
        n = len(arr)
        count = 0

        for i in range(n):
            mini = i
            for j in range(i + 1, n):
                if arr[j] < arr[mini]:
                    mini = j

            if mini != i:
                arr[mini], arr[i] = arr[i], arr[mini]
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    # input:
    a = [2, 8, 5, 4]

    # output: 1
    print(sol.minSwaps(a))
