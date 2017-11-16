#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main():
	cur_x = 0
	cur_y = 0
	rows  = 10
	cols  = 10
	terminal = [[""] * cols ] * rows
	insert_mode = False
	chars = ""
	
	cef = open(input(), "r")
	for lines in cef:
		for i in range(len(lines)):
			curr = lines[i]
			if curr == "^":
				i+=1
				currNext = lines[i]
					
				#do processing
				ch = currNext
				print(ch)
				if ch == "c":
					terminal = [[''] * 10] * 10		
				elif ch == "h":
					cur_x, cur_y = 0, 0
				elif ch == "b":
					cur_x = 0
				elif ch == "d":
					if cur_y < rows - 1:
						cur_y += 1
				elif ch == "u":
					if cur_y > 0:
						cur_y -= 1
				elif ch == "l":
					if cur_x > 0:
						cur_x -= 1
				elif ch == "r":
					if cur_x < cols - 1:
						cur_x += 1
				elif ch == "e":
					for a in range(cur_x, cols):
						terminal[cur_y][a] = ''
				elif ch == "i":
					insert_mode = True
				elif ch == "o":
					insert_mode = False
				elif ch == "^":
					chars = "^"
				elif ch in range(1,10):
					print(ch +" here")
					
					cur_y = int(ch)
					i += 1
					cur_x = int(lines[i])
				#end processing	
				
			else:
				chars = curr
				
			if len(chars) > 0:
				if insert_mode:
					terminal[cur_y][cur_x] = chars
				else:
					for a in range(cols-1, cur_x, -1):
						terminal[cur_y][a] = terminal[cur_y][a-1]
					terminal[cur_y][cur_x] = chars
			if cur_x < cols - 1:
				cur_x += 1
				
        print(terminal)				
	'''							
	for line in terminal:
		print("".join(line))
	print(terminal)
	'''	
			
	
	
	return 0

if __name__ == '__main__':
	main()

