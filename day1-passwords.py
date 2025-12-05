# Day 1: Passwords
# Take input, first char is Left or right
# if get to 99 next is 0, if moving backwards get to 0 next is 99. 
# counter for how many times you hit 0


# you may have large numbers and have to cross threshholds repeatedly

# PART 1: HOW MANY TIMES DID THE PASSWORD HIT 0


def part1_solution(filename, position, zero_counter):
    with open(file_name, "r") as instructions:
        for instruction in instructions:
            instruction = instruction.strip()
            turns = int(instruction[1:]) 
            side = instruction[0]
            if (side == "R"):
                position+=turns
                while(position > 99):
                    position = position - 100
            else:
                position-=turns 
                while(position < 0):
                    position = 100 + position

            if position == 0:
                zero_counter+=1

        print("The password for part 1 is ", zero_counter)

def part2_solution(filename, position, zero_counter):
    with open(file_name, "r") as instructions:
        for instruction in instructions:
            instruction = instruction.strip()
            turns = int(instruction[1:]) 
            side = instruction[0]
            if (side == "R"):
                position+=turns
                while(position > 99):
                    zero_counter += 1
                    position = position - 100
            else:
                position-=turns 
                while(position < 0):
                    zero_counter += 1
                    position = 100 + position
            if position == 0:
                    zero_counter +=1

        print("The password for part 2 is ", zero_counter)
# PART 2: HOW MANY TIMn ES DID IT PA
# got ans as 969





if __name__ == '__main__':
    file_name = "password-instructions.txt"
    problem_part = int(input("Which part of the problem is this?"))
    position = 50
    zero_counter = 0
    if problem_part == 1:
        part1_solution(file_name, position, zero_counter)
    else:
        part2_solution(file_name, position, zero_counter)
             


