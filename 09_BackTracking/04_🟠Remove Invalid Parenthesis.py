
def check_valid_parnt(s):
    st = []
    n = len(s)

    for i in range(n):
        if s[i] == '(' or s[i].isalpha():
            st.append(s[i])
        else:
            if not st:
                return False
            st.pop()
    
    return len(st) == 0





s = "()()()"
s = "(a)()()"
print(check_valid_parnt(s))