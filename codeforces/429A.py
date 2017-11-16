'''
4 2
aabb

6 3
aacaab
'''
from collections import Counter
nosOfBaloon, nosOfFriends = [int(x) for x in input().strip().split()]
allColors                 = Counter([x for x in input().strip()])
canBe = True
for k in allColors:
	if allColors[k] > nosOfFriends :		
		canBe = False
		break
	
print("YES" if canBe else "NO")		
		


