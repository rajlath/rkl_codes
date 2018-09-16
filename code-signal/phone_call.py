def phoneCall(min1, min2_10, min11, s):
    done = 0
    if s >= min1:
        done += 1
        s -= min1
    while s > min2_10 and done < 10:
        s -= min2_10
        done += 1
    if s >= min11:
        while s >=min11 and done >= 10:
            s -= min11
            done += 1
    #print(s)
    #if s > 0 : done+= 1
    return done

print(phoneCall(3,1,2,20))




