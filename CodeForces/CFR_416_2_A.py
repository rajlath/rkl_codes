vladik, valera = [int(x) for x in input().split()]
comp = int(vladik ** 0.5)

print(["Valera", "Vladik"][comp * (comp + 1)<= valera])
