from collections import deque

def min_max_substr(arr,k):
    mindq = deque()
    maxdq = deque()
    n = len(arr)

    total = 0
    i = 0
    j = 0

    while j < n:
        # remove useless from mindq
        while mindq and arr[j] <= arr[mindq[-1]]:
            mindq.pop()
        
        mindq.append(j)

        # remove useless from maxdq
        while maxdq and arr[j] >= arr[maxdq[-1]]:
            maxdq.pop()

        maxdq.append(j)


        # k size window
        if j-i+1 == k:
            mini = mindq[0]
            maxi = maxdq[0]
            total = total + arr[mini] + arr[maxi]

            if mindq and mindq[0] == i:
                mindq.popleft()
            
            if maxdq and maxdq[0] == i:
                maxdq.popleft()
        
            i += 1
        
        j += 1

    
    return total



if __name__ == "__main__":

    arr = [2, 5, -1, 7, -3, -1, -2]
    k = 4

    print(min_max_substr(arr,k))

