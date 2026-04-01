#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        n = len(arr)
        ans = []
        ans.append([arr[0]])
        
        for word in arr[1:]:
            isFound = False
            
            for grup in ans:
                if self.isanagram(word, grup[0]):
                    grup.append(word)
                    isFound = True
                    break
            
            if not isFound:
                ans.append([word])
        
        
        return ans
        
    
    
    def isanagram(self, s1,s2):
        dct1 = {}
        dct2 = {}
        
        for ch in s1:
            dct1[ch] = dct1.get(ch,0)+1
        
        for ch in s2:
            dct2[ch] = dct2.get(ch,0)+1
        
        
        return dct1 == dct2
        
        
    # more optimized solution:
    def anagrams_opt(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        n = len(arr)
        dct = {}
        
        for word in arr:
            
            freq = [0]*26
            for ch in word:
                idx = ord(ch)-ord('a')
                freq[idx] += 1
            
            key = tuple(freq)
            if key in dct:
                dct[key].append(word)
            else:
                dct[key] = [word]
        
        ans = []
        
        for key in dct:
            ans.append(dct[key])
        
        
        return ans
        


if __name__ == "__main__":
    sol = Solution()

    arr = ["act", "god", "cat", "dog", "tac"]
    print(sol.anagrams(arr))
    print(sol.anagrams_opt(arr))
    # Output: [['act', 'cat', 'tac'], ['god', 'dog']]

    