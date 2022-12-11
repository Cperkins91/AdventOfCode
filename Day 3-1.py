def main():
    ruck = [] # list containing all lines in file
    doubles = [] # list containing all the items in both compartments
    with open('rucksacks.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            ruck.append(line.strip())
    for i in ruck:
        tempDoubles = [] #Hold the doubles for a single line
        half =len(i) // 2 # Split each line into two halves
        halfOne = i[:half]
        halfTwo = i[half:]
        for j in halfOne: #Check for doubles in the compartments
            if j in halfTwo and j not in tempDoubles: # letter in both halves and not already in doubles list
                tempDoubles.append(j)
        doubles += tempDoubles #Add 1 instance of each double to the list
    sum = 0
    for k in range(len(doubles)):
        if doubles[k].isupper():
            sum += ord(doubles[k]) -38
        else:
            sum += ord(doubles[k]) - 96
    print (sum)
if __name__ == '__main__':
    main()
