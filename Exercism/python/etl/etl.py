#legacy_data = {1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],2: ["D", "G"],3: ["B", "C", "M", "P"],4: ["F", "H", "V", "W", "Y"],5: ["K"],8:["J", "X"],10: ["Q", "Z"] }

def transform(legacy_data):
    rets = {}
    for k, v in legacy_data.items():
        for kk in v:
            rets[kk.lower()] = k
    return rets

#print(transform({1: ["A", "E"], 2: ["D", "G"]}))




