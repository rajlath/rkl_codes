a, b , r = [int(x) for x in input().split()]
seq = list(range(1, r + 1))
for i in seq:
    if not i % a and not i % b:
        print("FizzBuzz")
    elif not  i % a:
        print("Fizz")
    elif not i %  b:
        print("Buzz")
    else:
        print(i)