def rotation(s1,s2):

    s = s1*2

    if s.find(s2) == -1:
        return False
    
    return True



# input:
s1 = "abcd"
s2 = "cdab"
# Output: true

print(rotation(s1,s2))