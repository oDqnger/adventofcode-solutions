with open("./puzzle_input.txt", "r") as f:
    lines = [x.strip().split(" ") for x in f.readlines()]

safe_reports = 0

for line in lines:
    is_increasing = False if int(line[0]) > int(line[-1]) else True
    is_safe = True
    s = False
    for index, cint in enumerate(line):
        cint = int(cint)
        if index == len(line) - 1:
            break
        if is_increasing:
            if not(1 <= (int(line[index + 1]) - int(line[index])) <= 3): 
                for i in range(len(line)):
                    if index == len(line) - 1:
                        s = True
                        break
                    if not(1 <= (int((line[:i]+line[i+1:])[index + 1]) - int((line[:i][i+1:])[index])) <= 3): 
                        is_safe = False
                        s = True
                        break

                if s:
                    break
        else:
            if not(1 <= (int(line[index])) - int(line[index + 1]) <= 3):
                for i in range(len(line[:i]+line[i+1:])):
                    if index == len(line) - 1:
                        s = True
                        break
                    if not(1 <= (int((line[:i]+line[i+1:])[index]) - int((line[:i][i+1:])[index + 1])) <= 3): 
                        is_safe = False
                        s = True
                        break

                if s:
                    break

    if is_safe:
        safe_reports += 1

print(safe_reports)
