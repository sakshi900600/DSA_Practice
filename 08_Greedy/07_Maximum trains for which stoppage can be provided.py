class Solution:
    def maxStop(self, train, plat, trains):
        #code here
        
        # n = train , m = plat , trains = [arr, dept, plat]
        # print(train, plat)
        
        m = plat
        
        trains.sort(key=lambda x: x[1])
        platform_arr = [0]*(m+1)
        
        count = 0
        for train_det in trains:
            arr = train_det[0]
            dept = train_det[1]
            platform = train_det[2]
            
            if platform_arr[platform] == 0:
                platform_arr[platform] = dept
                count += 1
            else:
                last_dept = platform_arr[platform]
                if last_dept <= arr:
                    platform_arr[platform] = dept
                    count += 1
        
        return count
        
        

if __name__ == "__main__":
    sol = Solution()

    trains = [[900, 910, 1], [940, 1200, 1], [950, 1120, 2], [1100, 1130, 1], [1500, 1900, 2], [1800, 2000, 3]]

    # Output: 5
    print(sol.maxStop(6, 3, trains))  
