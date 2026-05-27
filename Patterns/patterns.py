
# ==================== PATTERNS ====================

# 1.
# * * * *
# * * * *
# * * * *
# * * * *

# 2.
# *
# * * 
# * * *

# 3. 
# 1
# 1 2
# 1 2 3

# 4.
# 1
# 2 2 
# 3 3 3 

# 5. 
# * * *
# * *
# *

# 6. 
# 1 2 3
# 1 2
# 1


# 7. 
#     *
#   * * *
# * * * * *


# 8. 
# * * * * *
#   * * *
#     *


# 9. 
#     *
#   * * *
# * * * * *
# * * * * *
#   * * *
#     *


# 10.
# *
# * * 
# * * *
# * *
# *


# 11. 
# 1 
# 0 1
# 1 0 1


# 12. 
# 1         1
# 1 2     2 1
# 1 2 3 3 2 1 


# 13. 
# 1
# 2 3
# 4 5 6

# 14.
# A
# A B 
# A B C 


# 15.
# A B C
# A B
# A

# 16.
# A 
# B B
# C C C


# 17.
# A B C
# B C
# C


# 18.
# A 
# B C 
# C D E 


# 19.
#    A
#  A B A
# A B A B A


# 20.
# C
# B C
# A B C


# 21.
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *


# 22.
# * * *
# *   *
# * * *


# 23.
# * * * * * *
# * *     * *
# *         *
# *         *
# * *     * *
# * * * * * *


# 24.
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3




# ====================== SOLUTIONS ===========================

def p1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
            

def p2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()


def p3(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()


def p4(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()


def p5(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print("*", end=" ")
        print()


def p6(n):
    for i in range(n,-1,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()


def p7(n):
    for i in range(1,n+1):
        # space
        for sp in range(n-i):
            print(" ", end=" ")
        
        for st in range(2*i-1):
            print("*", end=" ")
        
        print()


def p8(n):
    for i in range(n, -1, -1):
        # space
        for sp in range(n-i):
            print(" ", end=" ")
        
        for st in range(2*i-1):
            print("*", end=" ")
        
        print()


def p9(n):
    p7(n)
    p8(n)


def p10(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
    
    for i in range(n-1, -1, -1):
        for j in range(i):
            print("*", end=" ")
        print()


def p11(n):
    for i in range(n):
        for j in range(i+1):
            if (i+j) % 2 == 0:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


def p12(n):

    cnt = 2
    for i in range(1, n+1):

        # left pattern
        for j in range(1, i+1):
            print(j, end=" ")

        # space
        for sp in range(2*n-cnt-1, -1, -1):
            print(" ", end=" ")
        
        cnt += 2

        # # right pattern
        for j in range(i,0,-1):
            print(j, end=" ")

        print()


def p13(n):
    cnt = 1
    for i in range(1, n+1):
        for j in range(i):
            print(cnt, end=" ")
            cnt += 1
        print()


def p14(n):
    cnt = ord('A')
    for i in range(n):
        for j in range(i+1):
            print(chr(cnt+j), end=" ")
        print()


def p15(n):
    cnt = ord('A')
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            print(chr(cnt+j), end=" ")
        print()


def p16(n):
    cnt = ord("A")
    for i in range(n):
        for j in range(i+1):
            print(chr(cnt), end=" ")
        cnt += 1
        print()


def p17(n):
    cnt = ord('A')
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            print(chr(cnt+j), end=" ")
        cnt += 1
        print()
        

def p18(n):
    cnt = ord('A')
    for i in range(n):
        for j in range(i+1):
            print(chr(cnt+j), end=" ")
        cnt += 1
        print()


def p19(n):
    cnt = ord("A")
    for i in range(n):
        # space
        for sp in range(n-i-1):
            print(" ", end=" ")
        
        # letters
        for j in range(i+1):
            print(chr(cnt+j), end=" ")
        
        for j in range(i-1, -1, -1):
            print(chr(cnt+j), end=" ")
        
        print()


def p20(n):
    cnt = ord('A')+ n-1
    # print(chr(cnt))

    for i in range(n):
        for j in range(i+1):
            print(chr(cnt+j), end=" ")
        cnt -= 1
        print()
        

def p21(n):

    # 1st half
    cnt = 2
    for i in range(n):
        # star
        for j in range(i+1):
            print("*", end=" ")
        
        # space
        for sp in range(2*n-cnt):
            print(" ", end=" ")
        
        cnt += 2

        # star
        for j in range(i+1):
            print("*", end=" ")
        
        print()


    # 2nd half
    cnt = 2
    for i in range(n-2, -1, -1):
        # star
        for j in range(i+1):
            print("*", end=" ")
        
        # space
        for sp in range(cnt):
            print(" ", end=" ")
        
        cnt += 2

        # star
        for j in range(i+1):
            print("*", end=" ")
        
        print()


def p22(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def p23(n):

    # 1st half
    cnt = 0
    for i in range(n-1, -1, -1):
        # star
        for j in range(i+1):
            print("*", end=" ")
        
        # space
        for sp in range(cnt):
            print(" ", end=" ")
        
        cnt += 2

        # star
        for j in range(i+1):
            print("*", end=" ")
        
        print()

    # 2nd half
    cnt = 2
    for i in range(n):
        # star
        for j in range(i+1):
            print("*", end=" ")
        
        # space
        for sp in range(2*n-cnt):
            print(" ", end=" ")
        
        cnt += 2

        # star
        for j in range(i+1):
            print("*", end=" ")
        
        print()


def p24(n):
    cnt = n

    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            bottom = j
            left = (2*n-2)-i
            right = (2*n-2)-j
            minDist = min(top, bottom, left, right)
            print(n - minDist, end=" ")
        print()
    

# fibonacci triangle pattern

def getfib(num):
    fibarr = [-1]*100

    fibarr[0] = 0
    fibarr[1] = 1

    for i in range(2,100):
        fibarr[i] = fibarr[i-1] + fibarr[i-2]
    
    return fibarr[num]

# print(getfib(5))


def p25(n):
    cnt = 0
    for i in range(n):
        for j in range(i+1):
            print(getfib(cnt), end=" ")
            cnt += 1
        print()

        


# function calls:
n = 4
# p1(n)
# p2(n)
# p3(n)
# p4(n)
# p5(n)
# p6(n)
# p7(n)
# p8(n)
# p9(n)
# p10(n)
# p11(n)
# p12(n)
# p13(n)
# p14(n)
# p15(n)
# p16(n)
# p17(n)
# p18(n)
# p19(n)
# p20(n)
# p21(n)
# p22(n)
# p23(n)
# p24(n)
p25(n)
