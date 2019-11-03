class Solution:
    def transformArray(self, arr) :
        begin, end = arr[0], arr[-1]
        while True:
            narr = [0]*(len(arr))
            narr[0] = begin
            narr[-1]= end
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    narr[i] = arr[i] + 1
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    narr[i] = arr[i] - 1
                else:
                    narr[i] = arr[i]

            if narr == arr:break
            else: arr = narr
        return arr
print(Solution().transformArray([1,6,3,4,3,5]))