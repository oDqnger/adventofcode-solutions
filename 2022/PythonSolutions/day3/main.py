import string

with open("./puzzle_input.txt", "r") as f:
    puzzle_input = f.readlines()

bool2 = False
char3 = ""
ans = 0

for line in puzzle_input:
    for char in line[:len(line) // 2]:
        for char2 in line[len(line) // 2:]:
            if char == char2:
                char3 = char
                break

    for x in string.ascii_letters:
        if char3 == x:
            ans += string.ascii_letters.index(x) + 1

print(ans)
