class Solution:
    def countBitsFlip(self, a, b):
        #code here
        
        # counting no of different bits.
        xor = a ^ b
        count = 0
        while xor:
            xor = xor & (xor-1)
            count += 1
        
        return count


if __name__ == '__main__': 
    a = 10
    b = 20
    sol = Solution()
    print(sol.countBitsFlip(a, b))
    # Output: 4

    