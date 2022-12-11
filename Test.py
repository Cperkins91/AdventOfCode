ruck = ['jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL']
doubles = []
for i in ruck:
    tempDoubles = []
    half = len(i) // 2  # Split each line into two halves
    halfOne = i[:half]
    halfTwo = i[half:]
    for j in halfOne:  # Check for doubles in the compartments
        if j in halfTwo and j not in tempDoubles:
            tempDoubles.append(j)
    doubles += tempDoubles
print(doubles)
sum = 0
for k in range(len(doubles)):
    if doubles[k].isupper():
        sum += ord(doubles[k]) - 38
    else:
        sum += ord(doubles[k]) - 96
print(sum)