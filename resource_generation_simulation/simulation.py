import time
import random

machines = {}
outputs = {}
endTime = 0
sfTicks = int(input("How many sf ticks per second on your sever (def 2): "))
ticks = 0
hours = float(input("How many hours should be simulated (decimals allowed): "))
endTicks = hours * 60 * 60 * sfTicks

for i in range(int(input("How many machines are you simulating: "))):
    machineName = input(f"What's the name of Machine {i + 1}: ")
    machine = {}
    machine["interval"] = int(input("How many ticks per generation attempt: "))
    machine["chance"] = float(input("What's the decimal chance to succeed (use 1 if every attempt): "))
    resources = []
    amounts = []
    chances = []
    output = {}
    for j in range(int(input(f"How many types of resources are made by {machineName}: "))):
        name = input(f"What's the name of resource {j + 1}: ")
        resources.append(name)
        amounts.append(int(input(f"How many {name} are generated: ")))
        chances.append(float(input(f"What's the decimal chance of generating {name}: ")))
        output[name] = 0
    machine["resources"] = resources
    machine["amounts"] = amounts
    machine["chances"] = chances
    machines[machineName] = machine
    outputs[machineName] = output

print("Simulating")
time.sleep(0.3)
print(".")
time.sleep(0.3)
print("..")
time.sleep(0.3)
print("...")

while (ticks < endTicks):
    for machineName, machine in machines.items():
        if not ticks % machine["interval"] == 0 or random.randint(1, 100) > machine["chance"] * 100:
            continue
        resource = random.choices(machine["resources"], weights=machine["chances"],k=1)[0]
        outputs[machineName][resource] += machine["amounts"][machine["resources"].index(resource)]
    ticks += 1

print(f"Simulation of {hours} Hour(s) Completed:")
for machineName, output in outputs.items():
    print(f"    {machineName}:")
    for resource, amount in output.items():
        print(f"        {resource}: {round(amount / hours, 2)} / hr")