def find_max_min(a):
    max = a[0]
    min = a[0]

    for i in a:
        if i > max:
            max = i
        
        if i<min:
            min = i

    return [max, min]

# input:
a = [1,2,3,4,5]
# output: 
[5, 1]
print(find_max_min(a))
