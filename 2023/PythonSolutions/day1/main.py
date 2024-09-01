import re

calibration_document = None
def part1(list1=None):

    DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7","8", "9", "10"]

    with open("./calibration_document.txt", "r") as f:
        calibration_document = f.readlines()

    temp_val = []
    final_ans = 0

    calibration_document = list1 if list1 != None else calibration_document

    for line in calibration_document:
        for char in line:
            if char in DIGITS:
                temp_val.append(char)

        final_ans += int(temp_val[0] + temp_val[-1])
        temp_val = []

    print(final_ans)

def part2():
    final_ans = 0

    DIGIT_IN_LETTERS = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight":'8',
        "nine": '9',
    }
    
    dict_one = {}

    with open("./calibration_document.txt", "r") as f:
        calibration_document = f.readlines()
    
    for line in calibration_document:
        for char, digit in DIGIT_IN_LETTERS.items():
            if char in line:
                if len([m.start() for m in re.finditer(char, line)]) > 1:
                    for x in [m.start() for m in re.finditer(char, line)]:
                        dict_one[digit] = x
                else:
                    dict_one[digit] = line.find(char)
            elif digit in line:
                if len([m.start() for m in re.finditer(digit, line)]) > 1:
                    for x in [m.start() for m in re.finditer(digit, line)]:
                        dict_one[digit] = x
                else:
                    dict_one[digit] = line.find(digit)
        
        dict_one = dict(sorted(dict_one.items(), key=lambda item: item[1]))
        final_ans += int(list(dict_one.keys())[0] + list(dict_one.keys())[-1])
        print(dict_one)
        dict_one = {}


    print(final_ans)

if __name__ == "__main__":
    part2()

