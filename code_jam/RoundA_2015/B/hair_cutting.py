def count_customers_served(T, barbers, times):
    if T < 0:return 0
    customers_served = 0
    for barber in range(barbers):
        customers_served += T // times[barber] + 1
    return customers_served

def get_barber_number(pos,barbers, times):
    low = -1
    high= 10000*pos
    while low + 1  < high:
        mid = (low + high) // 2
        if count_customers_served(mid, barbers, times) < pos:
            low = mid
        else:
            high = mid
    T = high
    customers_served_before = count_customers_served(T - 1, barbers, times)
    customer_to_be_served    = pos - customers_served_before
    for barber in range(barbers):
        if T % times[barber] == 0:
            customer_to_be_served -= 1
            if customer_to_be_served==0:
                return barber




inf = open("sample.in","r")
ouf = open("sample.ou","w")

nos_test_cases = int(inf.readline().strip())
for case in range(nos_test_cases):
    barbers,pos = [int(x) for x in inf.readline().strip().split()]
    times   = [int(x) for x in inf.readline().strip().split()]
    ouf.write("Case #{}: {} ".format(case+1, get_barber_number(pos, barbers, times)))
    ouf.write("\n")
