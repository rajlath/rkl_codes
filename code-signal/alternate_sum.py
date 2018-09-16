def alternatingSums(a):
    return [sum([x for x in a[0:len(a):2]]) , sum([x for x in a[1:len(a):2]])]

print(alternatingSums([50, 60, 60, 45, 70]))
