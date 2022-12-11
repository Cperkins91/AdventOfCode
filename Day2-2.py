def main():
    total = 0
    guide = []
    with open('strat.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            guide.append(line.strip())
    print (guide)
    for i in guide:
        a = i[0]
        b = i[2]
        sum = 0
        if b == 'Z': #Must Win
            sum += 6
            if a == 'A': # Opponent throws rock
                sum += 2 # You throw paper (2)
            elif a == 'B': # Opponent throws paper
                sum += 3 # You throw scissors (3)
            elif a == 'C': # Opponent throws scissors
                sum += 1 # You throw rock (1)
        elif b == "Y": #Must Draw
            sum += 3
            if a == 'A': #Opponent throws rock
                sum += 1 #You throw rock
            elif a == 'B': #Opponent throws paper
                sum += 2 # You throw paper
            elif a == 'C': #Opponent throws scissors
                sum+= 3 # You throw scissors
        elif b == 'X': #Must lose
            if a == 'A': #Opponent throws rock
                sum += 3 #You throw scissors
            elif a == 'B': #Opponent throws paper
                sum+=1 #You throw rock
            elif a == 'C': #Opponent throws scissors
                sum+= 2 #You throw paper
        total = total + sum
    print(total)

if __name__ == '__main__':
    main()