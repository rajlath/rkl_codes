nb_Test = int(input())
for _ in range(nb_Test):
    inside, boundary = [int(x) for x in input().split()]
    area = 2 * inside + boundary - 2
    print([area//2, int((area+0.5))//2][area%2 == 0])






