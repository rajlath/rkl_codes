'''
the Power Gem of purple color,
the Time Gem of green color,
the Space Gem of blue color,
the Soul Gem of orange color,
the Reality Gem of red color,
the Mind Gem of yellow color.
Examples
inputCopy
4
red
purple
yellow
orange
outputCopy
2
Time
Space
inputCopy
0
outputCopy
6
Power
Space
Soul
Mind
Time
Reality
'''
gems = ["Power","Time", "Space", "Soul", "Reality", "Mind"]
colors = ["purple", "green", "blue", "orange", "red", "yellow"]
total_colors = int(input())
for i in range(total_colors):
    gems[colors.index(input())]=""
gems = [x for x in gems if x != ""]
print(len(gems))
if len(gems)>0:
    print("\n".join(gems))





