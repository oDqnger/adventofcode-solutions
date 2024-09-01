with open("./puzzle_input.txt", "r") as f:
    puzzle_input = f.readlines()

red_cubes = 0
blue_cubes = 0
green_cubes = 0
final_ans = 0
temp_list = []
temp_list_2 = []
z = 0
game_num = 0

for game in puzzle_input:
    temp_list = game[(game.find(": ") + 2)::].replace("\n", "").split("; ")
    game_num = game.split(": ")[0].split(" ")[-1]
    for x in temp_list:
        temp_list_2 = x.split(", ")
        for y in temp_list_2:
            z = y.split(" ")
            if z[-1][-1] == "e":
                blue_cubes += int(z[0])
            elif z[-1][-1] == "d":
                red_cubes += int(z[0])
            elif z[-1][-1] == "n":
                green_cubes += int(z[0])    

    if red_cubes == 12 and blue_cubes == 14 and green_cubes == 13:
        final_ans += int(game_num)
        break
    elif red_cubes < 12 and blue_cubes < 14 and green_cubes < 13:
        final_ans += int(game_num)
    elif red_cubes > 12 or blue_cubes > 14 or green_cubes > 13:
        pass

print(final_ans)

