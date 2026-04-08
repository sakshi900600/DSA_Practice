# Weighted Job Scheduling

def getmaxprofit(jobs):
    jobs.sort()

    # return jobsec1(0,jobs)
    n = len(jobs)
    dp = [-1]*n
    return jobsec_memo(0,jobs,dp)


# approach-1
def jobsec1(idx, jobs):
    n = len(jobs)
    if idx >= n:
        return 0

    # non-overlapping next job
    # next = idx+1
    # while next < n and jobs[next][0] < jobs[idx][1]:
    #     next += 1

    # using binary search:
    next = getnext(jobs,idx)

    take = jobs[idx][2] + jobsec1(next,jobs)
    nottake = 0 + jobsec1(idx+1, jobs)

    return max(take, nottake)


# binary search to get next
def getnext(jobs, idx):
    n = len(jobs)
    si = idx+1
    ei = n-1

    while si <= ei:
        mid = (si+ei)//2

        if jobs[mid][0] >= jobs[idx][1]:
            ei = mid-1
        else:
            si = mid+1
    
    return si


# approach-2 memoization
def jobsec_memo(idx,jobs,dp):
    n = len(jobs)
    if idx >= n:
        return 0

    if dp[idx] != -1:
        return dp[idx]

    next = getnext(jobs,idx)
    take = jobs[idx][2] + jobsec_memo(next, jobs, dp)
    nottake = 0 + jobsec_memo(idx+1, jobs, dp)

    dp[idx] = max(take, nottake)
    return dp[idx]



# Inptut:
jobs = [[1, 2, 50], 
            [3, 5, 20],
            [6, 19, 100],
            [2, 100, 200]]

# Output: 250
print(getmaxprofit(jobs))
    