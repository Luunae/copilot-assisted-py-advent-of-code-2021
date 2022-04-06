def day_02a():
    # Get data from ./inputs/day_02.txt.
    # Format the data as a list of tuples, split on spaces.
    # The first element of each tuple is a one-word string.
    # The second element of each tuple is a one-digit integer.
    with open("./inputs/input_02.txt") as f:
        data = [tuple(line.split()) for line in f.readlines()]
        # cast the second element of each tuple to an int.
        data = [(x[0], int(x[1])) for x in data]
    # Initialize a position tuple. The first element is the x position. The second element is the y position.
    position = (0, 0)
    # The first element of each data tuple is a one-word string.
    # There are three possible directions: forward, down, and up.
    # forward increases the x position by the second element of the data tuple.
    # down increases the y position by the second element of the data tuple.
    # up decreases the y position by the second element of the data tuple.
    for direction, distance in data:
        if direction == "forward":
            position = (position[0] + distance, position[1])
        elif direction == "down":
            position = (position[0], position[1] + distance)
        elif direction == "up":
            position = (position[0], position[1] - distance)
    # Multiply the x position by the y position, then print the result.
    print(position[0] * position[1])


def day_02b():
    # Get data from ./inputs/input_02.txt.
    # Format the data as a list of tuples, split on spaces.
    # The first element of each tuple is a one-word string.
    # The second element of each tuple is a one-digit integer.
    with open("./inputs/input_02.txt") as f:
        data = [tuple(line.split()) for line in f.readlines()]
        # cast the second element of each tuple to an int.
        data = [(x[0], int(x[1])) for x in data]
    # Initialize a position tuple. The first element is the x position. The second element is the y position.
    position = (0, 0)
    # Initialize an int called aim.
    aim = 0
    # There are three commands: down, up, and forward.
    # down increases the aim by the second element of the data tuple.
    # up decreases the aim by the second element of the data tuple.
    # forward does two things:
    # 1. increases the x position by the second element of the data tuple.
    # 2. increases the y position by aim multiplied by the second element of the data tuple.
    for direction, distance in data:
        if direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        elif direction == "forward":
            position = (position[0] + distance, position[1] + aim * distance)
    # Multiply the x position by the y position, then print the result.
    print(position[0] * position[1])
