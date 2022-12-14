def main():
    count = 0
    lines = open('radio.txt', 'rt').read()
    for i in range(len(lines)):
        # a, b, c, d = lines[i], lines[i + 1], lines[i + 2], lines[i + 3]
        # slice = lines[i:i+4] #part 1
        slice = lines[i: i + 14]
        a = ''
        for j in slice:
            if j not in a:
                a += j
        if slice == a:
            print(f"The packet begins at {i + 14}")
            return 0


if __name__ == '__main__':
    main()
