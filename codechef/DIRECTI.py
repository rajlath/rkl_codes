for _ in range(int(input())):
    ways = int(input())
    answer = []
    dir, *map = [ x for x in input().split()]
    
    for i in range(1, ways):
        dir,*mapnow =  [ x for x in input().split()]
        current = ["Right ", "Left "][dir == "Right"]
        current += " ".join(map) 
        answer = [current] + answer
        map = mapnow
    answer = ["Begin "+ " ".join(map)] + answer
    print("\n".join(answer))
    
          