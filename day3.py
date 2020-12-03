"""
Part 1 = Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

Part 2 = In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""


def solve(right=3, down=1):
    sample = ("""
    .#..........#......#..#.....#.."
    ....#.............#.#....#..#..
    .....##...###....#..#.......#..
    .#....#..#......#........#.....
    .#.........###.#..........##...
    ...............##........#.....
    #..#..........#..##..#....#.#..
    ....#.##....#..#...#.#....#....
    ...###...#............#.#......
    #.........#..#...............#.
    """)
    # Grid = 32(W) * 323(H)
    f = open("day3.txt", "r")
    # Pattern goes Right 3, Down 1 and marks 'X if #' or 'O if .'
    # Prepare list
    fr = f.readlines()
    list1 = []
    for line in fr:
        list1.append(line)
    # Strips newline from each entry
    trees = list(map(str.rstrip, list1))
    return walkList(trees, right, down)


def walkList(input, right=3, down=1):
    sample = input  # pass the list as input
    # This is our pointer to each place in the array
    # Size of each entry in the list is 31, starting from 0
    # pointer = 35 # minus 31 = 4, which should be an X
    pointer = 0  # Initialize pointer position
    i = 0  # Initialize iterator position
    total_count = 0
    while i < len(sample):  # len(sample): # While i is less than the length of the table
        #  print(sample[i])    # prints the line of the sample data
        data = sample[i]
        value = data[pointer % len(data)]
        #  print(data[0])      # prints the data at that index
        #  print("Value at {},line{} = {}".format(pointer, i, value))
        if value == "#":
            total_count += 1

        i += down   # iterate to next line in the sample
        pointer += right # iterate over 3 places in line
    #  print("Total number of trees for values RIGHT {} DOWN {}: {}".format(right, down, total_count))
    return total_count


if __name__ == '__main__':
    print("Part 1, Total number of trees: {}".format(solve()))
    print("Part 2, Total number of trees: {}".format((solve()*solve(5,1)*solve(7,1)*solve(1,1)*solve(1,2))))
