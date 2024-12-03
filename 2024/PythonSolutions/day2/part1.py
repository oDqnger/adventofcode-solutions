with open("./puzzle_input.txt", "r") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]

safe_reports = 0

for line in lines:
    is_increasing = False if int(line[0]) > int(line[-1]) else True
    is_safe = True
    for index, cint in enumerate(line):
        cint = int(cint)
        if index == len(line) - 1:
            break
        if is_increasing:
            if not(1 <= (int(line[index + 1]) - int(line[index])) <= 3): 
                is_safe = False
                break
        else:
            if not(1 <= (int(line[index])) - int(line[index + 1]) <= 3):
                is_safe = False
                break

    if is_safe:
        safe_reports += 1

print(safe_reports)
