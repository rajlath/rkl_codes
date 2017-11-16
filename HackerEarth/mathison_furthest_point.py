class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class helpers():
    def manhattan_distance(self, a, b):
        '''
        a and b are instances of points class
        '''
        return abs(a.x - b.x) + abs(a.y - b.y)
        
    def in_interval(self, p, x, y):
        return x <= p and p <= y  
        
    def in_rectangle(self, p, x1, y1, x2, y2):
        '''
        
        x1 y1 are the top left corner and 
        x2 y2 are the bottom right corner
        for rectangle 
        p is the point to check for in this rectangle
        '''      
        
        return self.in_interval(p.x,x1, x2) and self.in_interval(p.y,y1,y2)
        
'''
10
1 299 1000 51 14 968 953
0 328 810
1 93 776 328 810 328 810
1 91 706 328 810 328 810
0 307 664
0 491 146
1 624 697 491 146 491 146
0 922 430
0 553 764
0 678 177
'''        
        
points = set() 
util   = helpers()       
for _ in range(int(input())):
    answer = -1
    qry = [int(x) for x in input().split()]
    if qry[0]==0:
        points.add(point(qry[1], qry[2]))
    else:
        ans = -1
        for pt in points:
            if util.in_rectangle(pt, qry[3],qry[4],qry[5],qry[6]):
                answer = max(answer, util.manhattan_distance(pt, point(qry[1],qry[2])))
        print("no point!" if answer==-1 else answer)                
            
                
    
                                          
        
