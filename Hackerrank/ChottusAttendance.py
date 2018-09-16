
def get_max(arr, n):
    result = arr[0]
    for i in range(1, n):
        if arr[i] > result:
            result = arr[i]
    return result

def possible(time, k, job, n)   :
    cnt = 1
    curr_time = 0
    for i in range(n):
        if curr_time + job[i] > time:
            curr_time = 0
            cnt += 1
        else:
            curr_time += job[i]
            i+= 1
    return cnt <= k

def solve(k, job, n):
    end = 0
    start = 0
    for i in range(n):
        end += job[i]
    ans = end
    job_max = get_max(job, n)
    while start <= end:
        mid = (start + end)//2
        if mid >= job_max and possible(mid, k, job, n):
            ans = min(ans, mid)
            end = mid - 1
        else:
            start = mid + 1
    return ans

n, k = 6, 4
arr  = [10, 7, 8, 12, 6, 8]
print(solve(k, arr, n))


