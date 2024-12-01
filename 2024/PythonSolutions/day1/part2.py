l_strip = []
r_strip = []
s_score = 0

with open("./puzzle_input.txt", "r") as f:
    for line in f:
        l_strip.append(int(line.strip().split("   ")[0]))
        r_strip.append(int(line.strip().split("   ")[-1]))

occ = 0

for num1 in l_strip:
    for num2 in r_strip:
        if num1 == num2:
            occ += 1
    s_score += num1 * occ
    occ = 0

print(s_score)
