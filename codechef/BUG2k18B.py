for _ in range(int(input())):
    hs, ms = [int(x) for x in input().split(":")]
    min_start = hs * 60 + ms
    min_need = int(input())
    ho, mo = [int(x) for x in input().split(":")]
    on_time = ho * 60 + mo
    offset  = int(input())
    print("Yes" if (min_start + min_need) <= (on_time  + offset) else "No")

