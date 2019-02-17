def raindrops(number):
    ans = str(number)
    ans1 = ''
    if number % 3 == 0: ans1 += "Pling"
    if number % 5 == 0:ans1 += "Plang"
    if number % 7 == 0:ans1 += "Plong"
    return ans if ans1 == "" else ans1
