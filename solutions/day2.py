'''
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''
import sys
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
max_colors = {"red":12, "green": 13, "blue": 14}
def part1(input):
    sum = 0
    with open(input) as f:
        for line in f:
            lst = line.split(":")
            id = int(lst[0].split(" ")[1])
            rounds = lst[1].split(";")
            fail = False
            for r in rounds:
                color = r.split(", ")
                for c in color:
                    x = c.split()
                    num_color, color_name = int(x[0]), x[1]
                    if num_color > max_colors[color_name]:
                        fail = True
                        break
                if fail: 
                    break
            if not fail:
                sum += id
    return sum

input_file = sys.argv[1]
result = part1(input_file)
print(result)


def part2(input):
    sum = 0
    with open(input) as f:
        for line in f:
            power = 1
            max_colors = {"red":0, "green": 0, "blue": 0}
            lst = line.split(":")
            id = int(lst[0].split(" ")[1])
            rounds = lst[1].split(";")
            for r in rounds:
                color = r.split(", ")
                for c in color:
                    x = c.split()
                    num_color, color_name = int(x[0]), x[1]
                    if num_color > max_colors[color_name]:
                        max_colors[color_name] = num_color
            for c, n in max_colors.items():
                power *= n
            sum += power
    return sum

result = part2(input_file)
print(result)

    






