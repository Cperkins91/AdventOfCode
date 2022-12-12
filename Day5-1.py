import numpy as np
import string


def main():
    instructions = []
    box = [""] * 9  # declare the 2d boxes array
    '''
    with open('stacks.txt', 'r') as file:
        lines = file.read()
    '''
    lines = open('stacks.txt', 'r').read()  # shorter way to read a file
    stacklines, movements = lines.split("\n\n")  # split the input at the empty line
    stacklines = stacklines.splitlines()  # split stacklines at the lines
    movements = movements.splitlines()
    for j in range(0, len(stacklines)-1):  # iterate through the rows of stacklines
        for i in range(1, len(stacklines[0]), 4):  # iterate through the cols
            box[i // 4] += (stacklines[j][i])
    for j in range(0, len(movements)):
        instruction = []
        for i in movements[j]:
            if i.isdigit():
                instruction.append((i))
        instructions.append(instruction)
    for i in instructions:
        print(i)

'''
    first = []
    for i in range(0,8):
        for j in range(0,8):
            box.append((j, stacks[i][1]))
        first = stacks[i][1]
        second = stacks[i][5]
        third = stacks[i][9]
        fourth
      
        while stacks[i][0] == '[': #iterate through the first part of the input
            temp = []  # set temp list to empty
            for j in stacks[i]: #iterate through the current line

                if j.isalpha(): #find the start of each box
                    temp.append(j) #append the number to temp
            box.append(temp)
            i += 1
    boxes = np.array(box).T
    print(boxes)
'''
if __name__ == '__main__':
    main()
