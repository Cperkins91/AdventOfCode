def main():
    instructions = []
    box = [""] * 9  # declare the 2d boxes array
    lines = open('stacks.txt', 'r').read()  # shorter way to read a file
    stacklines, movements = lines.split("\n\n")  # split the input at the empty line
    stacklines = stacklines.splitlines()  # split stacklines at the lines
    movements = movements.splitlines()
    for j in range(0, len(stacklines)-1):  # iterate through the rows of stacklines
        for i in range(1, len(stacklines[0]), 4):  # iterate through the cols
            box[i // 4] += (stacklines[j][i])
    for i in range(len(box)): #reverse the boxes to correct order
        box[i] = box[i][::-1]
        box[i] = box[i].strip() #strip out spaces
    for j in range(0, len(movements)): #iterate through movements
        instruction = []
        x = movements[j].split() #split the line
        for i in x:
            if i.isdigit(): #extract the numbers from the instruction line
                instruction.append(i)
        instructions.append(instruction)
    for i in instructions:
        temp = box[int(i[1])-1][-int(i[0]):] #select the last x boxes in column y per instruction
        #temp = temp[::-1] #reverse the boxes (use for part 1)
        box[int(i[2])-1] += temp #append moved boxes to new column
        box[int(i[1])-1] = box[int(i[1])-1][0:-int(i[0])] #remove the moved boxes from the initial column
    answer = ''
    for i in box:
        answer += i[-1]
    print(answer)

if __name__ == '__main__':
    main()
