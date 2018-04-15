
'''
"%@#$ $#@ __= 556 1900"
"$$=50"

"a "
"a"

" a "
"a"


"   "
""
'''
decoded = ''
ins = input()[1:-1]

encoded = [x for x in ins.split(' ')]
for i, x in enumerate(encoded):
    if len(x)==1:
        decoded += x
    else:
        if i%2==1:
            decoded += x[0]
        else:
            decoded += x[-1]
print('"'+decoded+'"')
