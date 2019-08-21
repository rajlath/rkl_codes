def perfectCity(departure, destination):
    ans = abs(departure[0] - departure[1])
    ans+= abs(departure[1] - destination[1])
    ans+= abs(destination[0] - departure[1])
    return ans

print(perfectCity([0.4, 1], [0.9, 3]))