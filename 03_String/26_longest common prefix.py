
def longest_common_prefix(strs):
    strs.sort()

    first_str = strs[0]
    last_str = strs[-1]

    n = len(first_str)
    m = len(last_str)

    ans = ""

    for i in range(min(n,m)):
        if first_str[i] == last_str[i]:
            ans += first_str[i]
        else:
            break

    # print(ans)

    return ans


strs = ["flower","flow","flight"]
# Output: "fl"

strs = ["dog","racecar","car"]
# Output: ""

print(longest_common_prefix(strs))
