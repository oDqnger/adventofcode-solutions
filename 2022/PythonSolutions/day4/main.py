def part1(): 
    with open("./puzzle_input.txt", "r") as f:
        puzzle_input = f.readlines()
   
    final_ans = 0
    first_good_pair = ""
    last_good_pair = ""

    for line in puzzle_input:
        first_pair, last_pair = line.split(",")[0].removesuffix("\n"), line.split(",")[1].removesuffix("\n")
        for x in range(int(first_pair.split("-")[0]), int(first_pair.split("-")[-1]) + 1):
            first_good_pair += str(x)    
        for y in range(int(last_pair.split("-")[0]), int(last_pair.split("-")[-1]) + 1):
            last_good_pair += str(y)
       
        if first_good_pair in last_good_pair or last_good_pair in first_good_pair:
            
            print(first_good_pair)
            print(last_good_pair)
            final_ans += 1

        first_good_pair = ""
        last_good_pair = ""

    print(final_ans)

def part2():
    pass

if __name__ == "__main__":
    part1()
