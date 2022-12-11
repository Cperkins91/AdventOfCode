'''
find the largest sum in a list. Each set is seperated with a blank line.
'''

def main():
    food = []
    sums = []
    max = 0
    sum = 0
    index = 0
    with open('input.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            food.append(line.strip())
        for i in range(len(food)): #iterate through the list
            if food[i] != '':
                sum = sum + int(food[i])
            else:  # if a blank line
                sums.append(sum)
                sum = 0
        nsums = sorted(sums)
        print(nsums[-1])
        total = nsums[-3] + nsums[-2] +nsums [-1]
        print(total)
'''
def main():
    food = []
    max = 0
    sum = 0
    index = 0
    with open('input.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            food.append(line.strip())
        for i in range(len(food)): #iterate through the list
            if food[i] != '':
                sum = sum + int(food[i])
            else:  # if a blank line
                if sum > max: # check if new sum is larger than old total
                    max = sum #set total to new highest sum
                    sum = 0 #reset sum to 0
                    index = i
        print(max)
        print(f"the index of the largest sum is {index}")
'''
main()