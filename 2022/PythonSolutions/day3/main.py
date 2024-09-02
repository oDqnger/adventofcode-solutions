import string

def part1():
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

def part2():
    with open("./puzzle_input.txt", "r") as f:
        puzzle_input = f.readlines()

    groups = []
    temp_list = []
    temp_num = 0
    list_of_letters = []
    ans = 0
    for line in puzzle_input:
        temp_list.append(line.removesuffix("\n"))
        temp_num += 1
        if temp_num == 3:
            groups.append(temp_list)
            temp_list = []
            temp_num = 0
    
    
    for x in range(len(groups)):
        for char in groups[x][0]:
            if char in groups[x][1] and char in groups[x][2]:
                list_of_letters.append(char)
                break
    

    for x in list_of_letters:
        ans += string.ascii_letters.index(x) + 1

    print(ans)

if __name__ == "__main__":
    part2()

