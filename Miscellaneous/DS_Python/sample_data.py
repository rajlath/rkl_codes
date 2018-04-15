import random
import string
def integer_array(size,  mins, maxs, steps=1):
    return random.sample(range(mins, maxs, steps),size)

def string_data(size, mode="ULD"):
        size = random.choice(range(1, size+1))
        if mode == "ULD":
            return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits,k=size))
        elif mode == "UL":
            return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase , k=size))
        elif mode == "U":
            return ''.join(random.choices(string.ascii_uppercase, k=size))
        elif mode == "L":
            return ''.join(random.choices(string.ascii_lowercase,k=size))
        elif mode == "D":
            return ''.join(random.choices(string.digits, k=size))

def string_arr_data(size, wsize,mode="D" ):
        arr = []
        for i in range(size):
            arr.append(string_data(wsize,mode))
        return arr

print(string_arr_data(10, 12))






