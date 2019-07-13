nb_test = int(input())
for _ in range(nb_test):
    current = input()
    answer  = "".join(sorted(current))
    
    if len(set(current)) == 1:answer = "-1"
    print(answer)
