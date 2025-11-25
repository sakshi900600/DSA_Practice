# here given a result string and 2 more string and we have to tell whether the result string is made up of the same char in the given 2 strings.

# example :
# first = "XY"
# second = "12"
# results = {"1XY2", "Y1X2", "Y21XX"}

# here: 1XY2-True  Y1X2-True  Y21XX-False (coz 1 extra X)


# 2 cond^n must satisfied:  len(result) = len(first)+ len(second),  result's all char must be either in first or second.

def sort_string(s):
    li = list(s)
    li.sort()

    ans = ""
    for i in li:
        ans += i
    
    return ans



def shuffle(first,second,result):
    if len(result) != len(first) + len(second):
        return False
    
    first = sort_string(first)
    second = sort_string(second)
    result = sort_string(result)

    i=0 # for first string
    j=0 # for second string
    k=0 # for result string

    while k != len(result):
        ch = result[k]

        if i<len(first) and first[i] == ch:
            i += 1
        elif j<len(second) and second[j] == ch:
            j += 1
        else:
            return False
        
        k += 1
    
    if i<len(first) or j<len(second):
        return False
    
    return True



first = "XY"
second = "12"
results = {"1XY2", "Y1X2", "Y21XX"}


for it in results:
    if shuffle(first,second,it) == True:
        print("Yes")
    else:
        print("No")





