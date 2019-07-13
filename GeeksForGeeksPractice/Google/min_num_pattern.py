def print_min_num_following_pattern(given):
    curr_max = 0
    last_num = 0
    for i in range(len(given)):
        if given[i] == "I":
            further_D = given[i+1:].count("D")
            if i == 0:
                curr_max = further_D + 2
                last_num += 1
                print(last_num, end=" ")
                print(curr_max, end=" ")
                last_num = curr_max
            else:
                curr_max = curr_max + further_D + 1
                last_num = curr_max
                print(last_num, end=" ")
            for k in range(further_D):
                last_num -= 1
                print(last_num, end=" ")
        if given[i] == "D":
            if i == 0:
                further_D = given[i+1:].count("D")
                curr_max = further_D + 2
                print(curr_max, end=" ")
                print(curr_max - 1, end=" ")
                last_num = curr_max - 1
            else:
                print(last_num, end=" ")
                last_num -= 1

print(print_min_num_following_pattern("ÏDID"))                
