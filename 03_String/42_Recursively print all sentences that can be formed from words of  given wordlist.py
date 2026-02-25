from typing import List


from typing import List


class Solution:
    def sentences(self, arr : List[List[str]]) -> List[List[str]]:
        # code here
        ans = []
        def helper(idx, path):
            if idx == len(arr):
                ans.append(path.copy())
                return
            
            for word in arr[idx]:
                path.append(word)
                helper(idx+1, path)
                path.pop()
        
        helper(0,[])
        
        return ans
                
        

if __name__ == "__main__":
    sol = Solution()

    wordList = [["you", "we"], ["have", "are"]]
    n = len(wordList)

    print(sol.sentences(wordList))

    # Output: 
    # [['you', 'have'], ['you', 'are'], ['we', 'have'], ['we', 'are']]

    