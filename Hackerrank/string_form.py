def print_formatted(number):
    n=number
    w=len(bin(n)[2:])+1

    for i in range(1,n+1):
        s=""
        s += str(i).rjust(w)
        s += oct(i)[2:].rjust(w)
        s += hex(i)[2:].upper().rjust(w)
        s += bin(i)[2:].rjust(w)
        print(s)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)        
