import math

# Part 1
print(
    math.prod(
        sum(i * (limit - i) > dist for i in range(dist))
        for limit, dist in zip([41,96,88,94], [214,1789,1127,1055])
    )
)

# Part 2
limit, dist = 41968894, 214178911271055
print(sum(i * (limit - i) > dist for i in range(limit)))