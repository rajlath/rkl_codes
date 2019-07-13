class Solutiion:
    def duplicateZeros(self, arr):
        curr = 0
        lens = len(arr)
        temp = arr[:]
        #x = 1
        for i, v in enumerate(temp):
            arr[curr] = v
            if v == 0:
                curr += 1
                if curr >= lens:break
                arr[curr] = 0
            curr += 1
            if curr >= lens:break
            #print(arr, x)
            #x += 1
    def duplicateZeros_1(self, arr)        :
        curr = 0
        temp = arr[:]
        lens = len(temp)
        for i in range(lens):
            if temp[i] == 0:
                if curr < lens:
                    arr[curr] = 0
                    curr += 1
                if curr < lens:
                    arr[curr] = 0
                    curr += 1
            else:
                if curr < lens:
                    arr[curr] = temp[i]
                    curr += 1
        return arr

print(Solutiion().duplicateZeros_1([1,0,2,3,0,4,5,0]))
