nod = input()
dislikes = []
for x in range(nod):
    dislikes.append(raw_input())
now = input()
sent = raw_input().split()
output = []
for x in sent:
    if x in dislikes:
        continue
    output.append(x[0].upper())
print ".".join(output)
