# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    
    for i in arr:
        if not ispalindrome(i):
            return False
    
    return True
    
def ispalindrome(num):
    s = str(num)
    
    if s != s[::-1]:
        return False
    
    return True


# Input: 
arr = [111, 222, 333, 444, 555]
# Output: true

print(isPalinArray(arr))