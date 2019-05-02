a, b, c = 13, 17, 19
peri = sum([a, b, c]) // 2
print(peri)
ar =int((peri * (peri - a) * (peri - b) + (peri - c))  ** 0.5)
print(ar * ar * 16)
print(189555 ** 0.5 // 16)