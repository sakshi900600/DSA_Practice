from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        dct = {}
        q = deque()
        ans = ""
        n = len(s)

        for i in range(n):
            ch = s[i]
            dct[ch] = dct.get(ch, 0) + 1

            if dct[ch] == 1:
                q.append(ch)

            while q and dct[q[0]] > 1:
                q.popleft()

            if q:
                ans += q[0]
            else:
                ans += '#'

        return ans



if __name__ == "__main__":
    s = "abadbc"
    sol = Solution()
    print(sol.firstNonRepeating(s))
    # Output: "aabbdd"
