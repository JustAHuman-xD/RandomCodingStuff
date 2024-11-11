import math
import random

machines = {}
simulations = {}
endTime = 0
sfTicks = int(input("(def 2) SF Tps: "))
ticks = 0
hours = float(input("Hours to Simulate: "))
endTicks = math.floor(hours * 60 * 60 * sfTicks)

for i in range(int(input("# of Simulated Machines: "))):
    machineName = input(f"Machine {i + 1} Name: ")
    machine = {}
    machine["interval"] = int(input("Generation Interval: "))
    machine["chance"] = float(input("Generation Chance %: "))
    outputs = []
    amounts = []
    weights = []
    simulated = {}
    for j in range(int(input(f"{machineName} # of Outputs: "))):
        name = input(f"Output {j + 1} Name: ")
        outputs.append(name)
        amounts.append(int(input(f"{name}'s Amount:")))
        weights.append(float(input(f"{name}'a Weight: ")))
        simulated[name] = 0
    machine["outputs"] = outputs
    machine["amounts"] = amounts
    machine["weights"] = weights
    machines[machineName] = machine
    simulations[machineName] = simulated

print()
print("Simulating 0.00%",end="")

progress = 0.00
updateInterval = max(1, math.floor(endTicks / 10000))
while (ticks < endTicks):
    for machineName, machine in machines.items():
        if not ticks % machine["interval"] == 0 or random.randint(1, 100) > machine["chance"]:
            continue
        resource = random.choices(machine["outputs"], weights=machine["weights"],k=1)[0]
        simulations[machineName][resource] += machine["amounts"][machine["outputs"].index(resource)]
    if ticks % updateInterval == 0:
        progress = round(ticks / endTicks * 100, 2)
        print(f"\rSimulating {progress}%", end="")
    ticks += 1

print("\rSimulating 100.00%\n")
print("########################################")
print(f"Simulation of {hours} Hour(s) Completed:")
for machineName, simulated in simulations.items():
    print(f"    {machineName}:")
    for resource, amount in simulated.items():
        print(f"        {resource}: {round(amount / hours, 2)} / hr")
print("########################################")