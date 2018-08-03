var a = parseInt(readline());
var b = parseInt(readline());
distance = Math.abs(a - b);
for_a = parseInt(distance / 2);
for_b = distance - (for_a);
print(distance, for_a, for_b)
var ans = 0;
ans += parseInt(for_a * (for_a - 1) / 2);
ans += parseInt(for_b * (for_b - 1) / 2);
print(ans)