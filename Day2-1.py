def main():
    total = 0
    guide = []
    with open('strat.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            guide.append(line.strip())
    print (guide)
    '''
    A/X = Rock 1
    B/Y = Paper 2
    C/Z = Scissors 3
    '''
    for i in guide:
        sum = 0
        a = i[0]
        b = i[2]
        if b == 'X': #Points for what you threw
            sum += 1
        elif b == 'Y':
            sum += 2
        elif b == 'Z':
            sum += 3
        if i == 'A Y' or i == 'B Z' or i == 'C X': #Winning combinations
            sum += 6
        elif i == 'A X' or i == 'B Y' or i == 'C Z': #Draw combinations
            sum += 3
        total = total +sum
    print(total)

if __name__ == '__main__':
    main()