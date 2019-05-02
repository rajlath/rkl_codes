import statistics
import numpy
nb_boys, k = [int(x) for x in input().split()]
ins = [int(x) for x in input().split()]
for i in range(nb_boys - k + 1):
    curr = numpy.array(ins[i:i+k])
    ans  = "{:.6f}".format(numpy.std(curr))
    print(ans, end=" ")

