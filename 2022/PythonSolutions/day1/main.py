def part1():
    with open("./puzzle_input.txt", "r") as f:
        puzzle_input = f.readlines()

    better_list = []
    temp_list = []

    for line in puzzle_input:
        if line != "\n":
            temp_list.append(line.removesuffix("\n"))
        else:
            better_list.append(temp_list)
            temp_list = []

    final_calorie = 0
    temp_calorie = 0

    for list1 in better_list:
        for calorie in list1:
            temp_calorie += int(calorie)

        if final_calorie <= temp_calorie:
            final_calorie = temp_calorie

        temp_calorie = 0

def part2():
    with open("./puzzle_input.txt", "r") as f:
        puzzle_input = f.readlines()

    better_list = []
    temp_list = []

    for line in puzzle_input:
        if line != "\n":
            temp_list.append(line.removesuffix("\n"))
        else:
            better_list.append(temp_list)
            temp_list = []    

    calorie_list = []
    temp_calorie = 0
    final_calorie = 0

    for list1 in better_list:
        for calorie in list1:
            temp_calorie += int(calorie)

        calorie_list.append(temp_calorie)
        temp_calorie = 0
    
    for x in range(0,3):
        final_calorie += max(calorie_list)
        calorie_list.remove(max(calorie_list))

    print(final_calorie)

if __name__ == "__main__":
    part2() 
