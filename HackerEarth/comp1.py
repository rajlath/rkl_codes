def main():
    for _ in range(int(input())):
        rc = int(input())
        center = rc // 2 
        for i in range(rc):
            curr = [x for x in input().split()]
            try:
                indx = curr.index("*")
                por = i
                poc = indx
                break
            except:
                continue    
            
               
        ans = (abs(center - por) + abs(center - poc))        
        print(ans)
        
main()        
        
