class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '%d %d' % (self.x, self.y)
        
        
def is_in_poly(vs, p):
    
    wn = 0  

    for i in range(len(vs) - 1):
        v0, v1 = vs[i], vs[i + 1]
        
        def on_line_x():
            if v0.x <= v1.x:
                return v0.x <= p.x and p.x <= v1.x

            return v0.x >= p.x and p.x >= v1.x

        
        def left_or_right():
            return ((v1.x - v0.x) * (p.y - v0.y)) - ((v1.y - v0.y) * (p.x - v0.x))

        if v1.y >= p.y and p.y > v0.y:  
            lor = left_or_right()
            if lor > 0:
                wn += 1
            elif lor == 0:
                return True
        elif v0.y >= p.y and p.y > v1.y:  
            lor = left_or_right()
            if lor < 0:
                wn -= 1
            elif lor == 0:
                return True
        elif v0.y == p.y and on_line_x():  
            return True

    return wn != 0        
        
        
cef = open("prisoner.txt", "r") 
for lines in cef:
	lines.rstrip("\r\n")  
	coords,_, xy = lines.rpartition("|")     
	coord = list()
	for x in coords.split(","):
		a, b = x.split()
		coord.append(Point(int(a), int(b)))
	coord.append(coord[0])
	
	x, y = xy.split()
	tp   = Point(int(x), int(y))
	print("Prisoner" if is_in_poly(coord, tp) else "Citizen")
	
        
        
