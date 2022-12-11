import re


def main():
    assignments = []
    sum = 0
    with open('assignments.txt', 'rt') as file:
        lines = file.readlines()
        for line in lines:
            assignments.append(line.strip())
    for i in assignments:
        nums = []
        nums = re.findall(r'\d+', i)
        if int(nums[0]) > int(nums[3]) or int(nums[1]) < int(nums[2]): #if range 1 > 2 or range 1 < 2
                #and int(nums[2]) > int(nums[3]) or int(nums[3]) < int(nums[0]): #if range 2 > 1 or 2 < 1
            print(f"Found one in the line: {nums}")
            sum += 1
    print(len(assignments)-sum)


if __name__ == '__main__':
    main()
