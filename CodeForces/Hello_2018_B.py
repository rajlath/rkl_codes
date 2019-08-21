vertices = int(input())
leafs = [-1] + [int(input()) -1 for _ in range(vertices - 1)]
grp1 = [0] * vertices
for i in range(1, vertices):
    grp1[leafs[i]] += 1
grp2 = [0] * vertices
for i in range(1, vertices):
    if grp1[i] == 0:
        grp2[leafs[i]] += 1
answer = "Yes"
for i in range(vertices):
    if grp1[i] > 0 and grp2[i] < 3:
        answer = "No"
print(answer)        
