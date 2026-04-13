

def roti_prata(p, rank):
    si = 0
    # ei -> the max time on which the chef will make at least p paratha
    # take to make paratha is: r,2r,3r,4r,...pr  where r is rank
    # it can be written as r(1+2+3+4....p)
    # r *(p(p+1))/2

    # now the chef which will take the maxm time to cook, their rank will be considered for the worse case. i.e chef with the largest rank

    ei = max(rank) * (p*(p+1))//2

    ans = -1
    while si <= ei:
        mid = (si+ei)//2

        if cancook(p,rank,mid):
            ans = mid
            ei = mid-1
        else:
            si = mid+1
    

    return ans



def cancook(p, rank, time):

    total_prata = 0

    for r in rank:
        t = 0
        prata = 0
        i = 1

        while True:
            next_time = i*r

            if t+next_time > time:
                break

            prata += 1
            t += next_time
            i += 1
        
        total_prata += prata
        
        if total_prata >= p:
            return True
    
    return False



# input:
p = 10
rank = [1,2,3,4]
# Output:12

p = 8
rank = [1]
# Ouptut: 36

print(roti_prata(p, rank))