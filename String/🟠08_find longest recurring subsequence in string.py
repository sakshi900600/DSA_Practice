# print(5 & 1)
# print(4 & 0)


s = "abc"
n = len(s)
ans = []

for i in range(1<<n):
    subseq = ""

    for j in range(n):
        if i & 1<<j:
            subseq += s[j]

    ans.append(subseq)


print(ans)