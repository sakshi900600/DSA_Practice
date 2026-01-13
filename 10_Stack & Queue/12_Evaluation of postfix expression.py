class Solution:
    def evaluatePostfix(self, arr):
        # code here
        
        st = []
        n = len(arr)
        operator = ["+", "-", "*", "/", "^"]
        
        for i in range(n):
            if arr[i] not in operator:
                st.append(int(arr[i]))
            else:
                op = arr[i]
                top2 = st.pop()
                top1 = st.pop()
                
                if op == "+":
                    res = top1 + top2
                elif op == "-":
                    res = top1 - top2
                elif op == "*":
                    res = top1 * top2
                elif op == "/":
                    res = top1 // top2
                elif op == "^":
                    res = top1 ** top2
                
                st.append(res)
        
        
        return st[-1]
                
        
                
        

if __name__ == "__main__":
    # input:
    arr = ["2", "3", "1", "*", "+", "9", "-"]
    obj = Solution()
    res = obj.evaluatePostfix(arr)
    print(res)

    # Output: -4