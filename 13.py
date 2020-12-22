with open("input/13.txt") as f:
    earliest_time = int(f.readline())
    schedule = [int(i) if i.isnumeric() else i for i in f.readline().split(",")]

earliest_bus_id = 0
earliest_bus_time = 999999999999999999

product = 1

for bus in schedule:
    if bus == "x":
        continue

    product *= bus
    
    next_bus_time = ((earliest_time // bus) * bus) + bus
    if next_bus_time < earliest_bus_time:
        earliest_bus_id = bus
        earliest_bus_time = next_bus_time

print(f"Earliest Bus Wait x ID: {earliest_bus_id * (earliest_bus_time - earliest_time)}")

x = 0
for i in range(len(schedule)):
    bus = schedule[i]
    if bus == "x":
        continue

    n = (product // bus)
    x += -i * n * pow(n, -1, bus)

answer = x % product

print(f"Competition Answer: {answer}")