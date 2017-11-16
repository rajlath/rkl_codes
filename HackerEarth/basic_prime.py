n = int(input())
print(' '.join(map(str,[x for x in range(2,100) if not [t for t in range(2,x) if not x%t]])))
            
