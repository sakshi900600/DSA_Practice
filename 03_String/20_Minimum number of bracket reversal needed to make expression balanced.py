#User function Template for python3
def countminreversals(s):
    
    openb = 0
    closeb = 0
    
    for ch in s:
        if ch == '{':
            openb += 1
        else:
            if openb > 0 : # balanced so remove it
                openb -= 1
            else:
                closeb += 1 # unbalanced
    
    if (openb + closeb) % 2!=0:
        return -1
        
    
    if openb % 2 == 0:
        openb = openb // 2
    else:
        openb = (openb+1)// 2 
    
    if closeb % 2 == 0:
        closeb = closeb // 2
    else:
        closeb = (closeb+1) // 2 
        
    
    return openb + closeb 
        
        
    
    
if __name__ == "__main__":

    s = "}{{}}{{{"
    print(countminreversals(s)) 
    # Output: 3
    
    
    