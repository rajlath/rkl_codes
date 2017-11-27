'''
4
A..A..B...B
..A..
A....A
..B..B..B..
'''

for _ in range(int(input())):
    curr = list(input())
    cnt_a = 0
    cnt_b = 0
    st_alpha = []
    st_dots  = []
    for i in curr:
        if i == "A" or i == "B":
            if i == "A":cnt_a += 1
            if i    == "B":cnt_b += 1
            if len(st_alpha)>0:
                last = st_alpha[-1]
                if last == i:
                    if i == "A":cnt_a += len(st_dots)
                    if i == "B":cnt_b += len(st_dots)
            st_alpha.append(i)
            st_dots = []

        else:
            st_dots.append(".")
    print(cnt_a, cnt_b)







'''
        if i in ["A", "B"]:
            if len(st_alpha) > 0:
                if st_alpha[-1] == i:
                    if i == "A":
                        cnt_a += len(st_dots)
                    else:
                        cnt_b += len(st_dots)
                    st_dots = []
                else:
                    print(i)
                    st_alpha.pop()
                    if i == "A":
                        cnt_a += 1
                        st_alpha.append("A")
                    elif i == "B":
                        cnt_b += 1
                        st_alpha.append("B")
        else:
            st_dots.append(".")
        print(st_dots, st_alpha)
    print(cnt_a, cnt_b)
'''

