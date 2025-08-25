def get_NbyK(arr,k):

    freq = {}
    li = []
    n = len(arr)

    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i],0)+1
    
    req_freq = n//k

    for k,v in freq.items():
        if v > req_freq:
            li.append(k)
    
    li.sort()
    print(li)
    # print(freq)


# Input: 
arr = [3, 4, 2, 2, 1, 2, 3, 3]
k = 4
# Output: [2, 3]

# arr = [9, 10, 7, 9, 2, 9, 10]
# k = 3

# Output: [9]


get_NbyK(arr,k)