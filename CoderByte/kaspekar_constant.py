
def KaprekarsConstant(num):
    counts = 0
    done = 0
    while num != 6174:
        aes = int("".join(sorted([x for x in str(num).zfill(4)])))
        des = int("".join(sorted([x for x in str(num).zfill(4)], reverse=True)))
        #print(aes, des)

        num = max(des, aes) - min(des, aes)
        counts += 1
        #if counts > 5:break
    # code goes here
    return counts

print(KaprekarsConstant(3524))

