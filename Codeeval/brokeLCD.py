import sys

numbers = [252, 96, 218, 242, 102, 182, 190, 224, 254, 246]
num = [0b11111100, 0b01100000, 0b11011010, 0b11110010, 0b01100110, 0b10110110, 0b10111110, 0b11100000, 0b11111110, 0b11110110, 0b00000001]
dumd = [int(x) for x in num]
print(numbers)
print(dumd)


def adjust(num):
	adjusted = []
	for i in num:
		if i == ".":
			adjusted[-1] -= 1
		else:
			adjusted.append(numbers[int(i)])
	return adjusted	
	
with open(input(), "r") as cef:
	lines = cef.readlines()
	for line in lines:
		matched = False
		leds, display = line.strip().split(";")			
		
		leds = leds.split(" ")
		inbin = [int(x, 2) for x in leds]
					
		display = adjust(display)
		print(display)
		print(inbin)
		
		matches = 0
		for i in range(len(leds) - len(display) + 1):
			for j in range(len(display)):				
				print(int(leds[i+j], 2)  , display[j])
				if int(leds[i+j], 2) & display[j] != display[j]:
					break
				else:
					matches +=1	
			if matches == len(display):
				matched = True
				break
	if not matched:
			print "0"	
		
			
			
		
	



