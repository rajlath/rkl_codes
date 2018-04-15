import base64
ans ="4261736536343A573268306448427A4F6938765A3239764C6D64734C305A525A465134544630"
code = ""
for i in range(0, len(ans), 2):
    curr = ans[i:i+2]
    curr = int(curr, 16)
    code += chr(curr)
print(code)
print(base64.b64decode("W2h0dHBzOi8vZ29vLmdsL0ZRZFQ4TF0"))