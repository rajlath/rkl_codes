
def is_prime(n):
    if n <=1 or n%2==0 or n%3==0:return False
    p = int(n ** 0.5)
    for i in range(5, p, 6):
        if n % i : return False
    return True

for _ in range(int(input())):
    print(["Not Prime", "Prime"][is_prime(int(input()))])



