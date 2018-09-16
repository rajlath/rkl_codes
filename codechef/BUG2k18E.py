for _ in range(int(input())):
   nop = int(input())
   plates = [x for x in input().split()]
   energy = [int(x) for x in input().split()]
   DP1 = [0] * (nop + 1)
   DP2 = [0] * (nop + 1)
   if plates[0] == "J":
       DP1[0] = energy[0]
       last = 1
   else:
       DP1[0] = energy[0]
       DP2[0] = energy[1]
   i = 1
   while i < nop:
       if plates[i] == "J":
           if last:
               DP2[i] = DP2[i-1] + energy[i]
               DP1[i] = DP1[i-1]
               last = 0
           else:
               DP1[i] = DP1[i-1] + energy[i]
               DP2[i] = DP2[i-1]
               last = 1
       else:
           while plates[i] == "F":
               DP1[i] = DP1[i-1] + energy[i]
               DP2[i] = DP2[i-1] + energy[i]
               i += 1
               if i > nop-1:break
           if i < nop-1:
               i += 1
               DP2[i] += energy[i]
               last = 1
           else:
               break


       i += 1

       #print(DP1, DP2)
   print(max(max(DP1), max(DP2)))





