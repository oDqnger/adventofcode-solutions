l_strip = []
r_strip = []
distance = 0

with open("./puzzle_input.txt", "r") as f:
    for line in f:
        l_strip.append(int(line.strip().split("   ")[0]))
        r_strip.append(int(line.strip().split("   ")[-1]))

while len(l_strip) > 0:
    distance += abs(min(l_strip) - min(r_strip))
    l_strip.pop(l_strip.index(min(l_strip)))
    r_strip.pop(r_strip.index(min(r_strip)))

print(distance)
