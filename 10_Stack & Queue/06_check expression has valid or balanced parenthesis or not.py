
# without stack
def valid_parenthesis(s):
    while "()"in s or "{}" in s or "[]" in s:
        s = s.replace('()', "")
        s = s.replace('{}', "")
        s = s.replace('[]', "")

    return len(s) == 0


# with stack
def balanced_parenthesis(s):
    st = []

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            st.append(ch)
        else:
            if not st:
                return False
            
            else:
                top = st[-1]
                if (ch==')' and top=='(') or (ch=='}' and top=='{') or (ch==']' and top=='['):
                    st.pop()
                else:
                    return False
    
    return len(st) == 0
 



s = "[{()}]"
# output: True

s = "([{]})"
# Output: False

# print(valid_parenthesis(s))
print(balanced_parenthesis(s))