# ADVENT OF CODE'


# Day 1: Passwords
# Take input, first char is Left or right
# if get to 99 next is 0, if moving backwards get to 0 next is 99. 
# counter for how many times you hit 0

# instruction = "R665"
# turns = int(instruction[1:]) 
# side = instruction[0]
# print(turns, side)


#open file and read line by line
position = 50
zero_counter = 0
with open("password-instructions.txt", "r") as instructions:
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

print("The password is ", zero_counter)



