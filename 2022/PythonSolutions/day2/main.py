
def part1():
    with open("./puzzle_input.txt", "r") as f:
        puzzle_input = f.readlines()

    opponent_play = []
    your_play = []
    points = 0

    for line in puzzle_input:
        opponent_play.append(line[0])
        your_play.append(line[2])

    for index, char in enumerate(opponent_play):
        if char == "A" and your_play[index] == "Y":
            points += 8
        elif char == "B" and your_play[index] == "Y":
            points += 5
        elif char == "C" and your_play[index] == "Y":
            points += 2
        elif char == "A" and your_play[index] == "X":
            points += 4
        elif char == "B" and your_play[index] == "X":
            points += 1
        elif char == "C" and your_play[index] == "X":
            points += 7
        elif char == "A" and your_play[index] == "Z":
            points += 3
        elif char == "B" and your_play[index] == "Z":
            points += 9
        elif char == "C" and your_play[index] == "Z":
            points += 6

def part2(): 
    with open("./puzzle_input.txt", "r") as f:
        puzzle_input = f.readlines()

    opponent_play = []
    your_play = []
    points = 0

    for line in puzzle_input:
        opponent_play.append(line[0])
        your_play.append(line[2])
    
    for index, char in enumerate(opponent_play):
        if char == "A" and your_play[index] == "Z":
            points += 8
        elif char == "A" and your_play[index] == "Y":
            points += 4
        elif char == "A" and your_play[index] == "X":
            points += 3
        elif char == "B" and your_play[index] == "Z":
            points += 9
        elif char == "B" and your_play[index] == "Y":
            points += 5
        elif char == "B" and your_play[index] == "X":
            points += 1
        elif char == "C" and your_play[index] == "Z":
            points += 7
        elif char == "C" and your_play[index] == "Y":
            points += 6
        elif char == "C" and your_play[index] == "X":
            points += 2

    print(points)

if __name__ == "__main__":
    part2()
