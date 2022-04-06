def day_02():
    # Get data from ./inputs/day_02.txt.
    # Format the data as a list of tuples, split on spaces.
    # The first element of each tuple is a one-word string.
    # The second element of each tuple is a one-digit integer.
    with open('./inputs/day_02.txt') as f:
        data = [tuple(line.split()) for line in f.readlines()]
