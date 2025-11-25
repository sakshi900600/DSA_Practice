
def histogram(a):
    max_area = a[0]
    n = len(a)

    for i in range(1,n):
        left_boundary = 0 
        k = i
        right_boundary = 0

        # left boundary
        while k>=0:
            if a[i] > a[k]:
                break
            if i != k:
                left_boundary += 1
            k -= 1
        
        # right boundary
        k = i
        while k<n:
            if a[i] > a[k]:
                break
            if i != k:
                right_boundary += 1
            k += 1

        
        area = a[i] * (right_boundary + left_boundary + 1)
        max_area = max(max_area,area)

    return max_area


def histogram_opt(a):
    max_area = 0
    st = [] # stack
    a = a +[0]

    n = len(a)
    i = 0
    while i<n:
        if not st or (a[i] >= a[st[-1]]):
            st.append(i)
            i += 1
        else:
            top = st.pop()
            height = a[top]

            if not st:
                width = i
            else:
                width = i-st[-1]-1
            
            area = height * width
            # print(area)

            max_area = max(max_area,area)
    
    return max_area





a = [10,6,2,5,3,10,3,4]
# print(histogram(a))

print(histogram_opt(a))