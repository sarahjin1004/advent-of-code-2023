
'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''
import re
import sys

def part1(input):
    sum = 0

    with open(input) as f:
        for line in f:
            match = re.findall(r'\d', line)
            first_digit, last_digit = match[0], match[-1]
            sum += int(first_digit) * 10 + int(last_digit)
    return sum

d = {
    "one":1,
    "two": 2,
    "three": 3,
    "four":4,
    "five":5, 
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def part2(input):
    sum = 0

    with open(input) as f:
        for line in f:
            number = ""
            first_digit, last_digit = None, None
            for char in line:
                if char.isdigit():
                    first_digit = int(char)
                    break
                else:
                    number  = number + char
                    for n in d:
                        if n in number:
                            first_digit = d[n]
                            break
                if first_digit:
                    break
            
            last_number = ""
            for char in line[::-1]:
                if char.isdigit():
                    last_digit = int(char)
                    break
                else:
                    last_number = char + last_number
                    for n in d:
                        if n in last_number:
                            last_digit = d[n]
                            break
                if last_digit:
                    break
            print(first_digit, last_digit)
            sum += int(first_digit) * 10 + int(last_digit)
    return sum


input_file = sys.argv[1]
result = part2(input_file)
print(result)

