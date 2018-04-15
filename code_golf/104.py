#import re;print("".join(sorted([x[0] for x in input().split() if re.match('\D[aeiou]',x)])))
import re;e="aeiou";n = "".join([x if x not in e else "*" for x in input()]);print("True" if n[0] not in e and len(re.findall(r'[a-z]{2}',n))==0 else "False")









