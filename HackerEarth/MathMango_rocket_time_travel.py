from math import log,log2
fusion = 2
fusion_energy = 0
drift = 1
steps = 0
drift_energy = 0
while True:
    fusion_energy += fusion
    drift_energy  += (drift * int(log2(fusion_energy)))
    print(fusion,drift, fusion_energy, drift_energy)
    fusion *= 4
    steps += 1
    drift *= 2
    if fusion_energy - drift_energy >= 300000000000000000:
        print(steps)
        break




