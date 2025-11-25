class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        max_val = 0
        items = []
        
        for i in range(len(val)):
            ratio = val[i] / wt[i]
            
            items.append((val[i], wt[i], ratio))
        
        items.sort(key=lambda x: x[2], reverse=True)
        
        
        for item in items:
            value = item[0]
            weight = item[1]
            ratio = item[2]
            
            if capacity >= weight:
                max_val += value
                capacity -= weight
            else:
                max_val += ratio * capacity
                capacity = 0
                break
                    
                    
        formatted_val = float(format(max_val, '.6f'))
        return formatted_val

        
        
        
if __name__ == "__main__":
    val = [60,100,120,30,200]
    wt = [10,20,30,50,10]
    cap = 50

    # output: 400.0
    sol = Solution()
    print(sol.fractionalKnapsack(val, wt, cap))