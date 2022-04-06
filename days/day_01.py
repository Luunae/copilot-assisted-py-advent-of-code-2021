def day_01a():
    # Get data input from ./inputs/day_01.txt as a list of integers
    with open("./inputs/input_01.txt", "r") as f:
        data = f.read().splitlines()
        data = [int(x) for x in data]
    increases = 0
    # Keep track of the number of times a value is greater than the previous value.
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            increases += 1
    print(increases)


def day_01b():
    # Get data input from ../inputs/day_01.txt as a list of integers
    with open("./inputs/input_01.txt", "r") as f:
        data = f.read().splitlines()
        data = [int(x) for x in data]
    # A Three-Measurement Window is a number that is equal to the sum of three consecutive variables.
    # data[i] + data[i+1] + data[i+2] is an example of a Three-Measurement Window.
    # Create a list of all Three-Measurement Windows.
    windows = []
    for i in range(len(data) - 2):
        windows.append(data[i] + data[i+1] + data[i+2])
    # Find the number of times a Three-Measurement Window is greater than the previous value.
    increases = 0
    for i in range(len(windows) - 1):
        if windows[i] < windows[i+1]:
            increases += 1
    print(increases)
