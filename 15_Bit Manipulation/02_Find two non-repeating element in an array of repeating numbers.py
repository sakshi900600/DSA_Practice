#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
		
		xor = 0
		for num in arr:
		    xor ^= num
		
		# rightmost set bit
		last_set_bit = xor & (-xor)
		
		# make 2 groups and also xor all group elem at the end in both group single elem will left.
		#  right_set_bit=1 and another 0 
		n1 = 0
		n2 = 0
		
		for num in arr:
		    if (num & last_set_bit):
		        n1 = n1 ^ num
		    else:
		        n2 = n2 ^ num
		
		li = [n1,n2]
		li.sort()
		
		return li
		    

if __name__ == '__main__':
    arr = [2, 4, 7, 9, 2, 4]
    sol = Solution()
    print(sol.singleNum(arr))
    # Output: [7, 9]

    