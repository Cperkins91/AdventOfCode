def main():
    ruck = []  # list containing all lines in file
    badges = [] # list containing all the badges the elves have
    with open('rucksacks.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            ruck.append(line.strip())
    for i in range(0, len(ruck), 3):
        tempBadges =[]
        for j in ruck[i]:
            if j in ruck[i + 1] and j in ruck[i + 2] and j not in tempBadges:
                tempBadges.append(j)
                break
        badges += tempBadges
    sum = 0
    for k in range(len(badges)):
        if badges[k].isupper():
            sum += ord(badges[k]) - 38
        else:
            sum += ord(badges[k]) - 96
    print(sum)

if __name__ == '__main__':
    main()