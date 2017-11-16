'''
5
1 2 3 4 5
9
'''


def computeLargestArea(hist, N):
    stack = []
     
    max_area = 0
     
    idx = 0
    while (idx < N):
        if not stack or hist[stack[-1]] <= hist[idx]:
            stack.append(idx)
            idx += 1
        else:
             
            height_idx = stack.pop()
             
            depth = idx
            if stack:
                depth = idx - stack[-1] - 1
             
            area = hist[height_idx] * depth
            max_area = max(area, max_area)
     
    while stack:
        print(idx)
        height_idx = stack.pop()             
        depth = idx
        if stack:
            depth = idx - stack[-1] - 1
        print(height_idx, depth)     
        area = hist[height_idx] * depth
        max_area = max(area, max_area)
             
    return max_area
 
def main():
    N = int(raw_input())
     
    hist = map(int, raw_input().split())
     
    print computeLargestArea(hist, N)
     
 
 
if __name__ == '__main__':
    main()