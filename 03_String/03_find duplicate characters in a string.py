def duplicate_char(s):
    dct = dict()

    for i in s:
        dct[i] = dct.get(i,0)+1
    
    for k,v in dct.items():
        if v > 1:
            li = []
            li.append(k)
            li.append(v)
            print(li)



s = "geeksforgeeks"
# Output: ['e', 4], ['g', 2], ['k', 2], ['s', 2]
    
duplicate_char(s)