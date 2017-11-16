def get_fact_zeros(m):
    power = 1
    zeros = 0
    while (5 ** power) <= m:
        zeros += m // (5**power)
        power += 1
    return zeros
    
def convert_to_base(num, base) :
    if num == 0 : return "0"
    s = ''
    while num:
        s = str(num%base)+s
        num//=base
    return s
    
def find_num_have_zeros(num_zero)    :
    num_infive = convert_to_base(num_zero, 5)
    fives = [5**y for y in range(len(num_infive))]
    sum_fives = sum(fives)
    for f in fives[:-1]:
        value = round(num_zero / sum_fives * f, 5)
        curr_f_val = int(value)
        num_zero -= curr_f_val
        sum_fives -= f
    return num_zero * 5
    
T = int(input())
for _ in range(T):
    t_zeroes = int(input())
    M = find_num_have_zeros(t_zeroes)
 
    # check if creating such a number is possible
    if get_fact_zeros(M) != t_zeroes:
        print(0)
        continue
 
    print(5)
    print(*[M + x for x in range(5)])
    
   
        

       
