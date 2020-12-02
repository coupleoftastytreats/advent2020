"""
To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest
number of times a given letter must appear for the password to be valid. For example,
1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b
 but needs at least 1. The first and third passwords are valid: they contain one a or nine c,
both within the limits of their respective policies.

How many passwords are valid according to their policies
"""

f = open("scratch.txt", "r")
fr = f.readlines()

def prepList(input, ver):
    # Modify each string with common delimiters
    new = input.replace(" ", "-")
    # print(new)
    # Pass each line as input here
    freq = new.split("-")
    # Define frequency lower and upper limit for each value to be checked
    lower = int(freq[0])  # Lower limit
    upper = int(freq[1])  # Upper limit
    value = freq[2].strip(":")
    password = freq[3]

    if ver == 1:
        if evalPartOne(value, password, lower, upper):
            return True
        else:
            return False

    if ver == 2:
        if evalPartTwo(value, password, lower, upper):
            return True
        else:
            return False


def selectOption(ver):
    total_count = 0
    for line in fr:
        try:
            if prepList(line, ver):
                total_count += 1
        except:
            pass
    return total_count


def evalPartOne(value, password, lower, upper):
    all_freq = {}

    for i in password:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    total = all_freq[value]

    if not total:
        pass
    elif lower <= total <= upper:
        return True
    else:
        return False


def evalPartTwo(value, password, lower, upper):
    upper = upper - 1
    lower = lower - 1
    checkLower = password[lower]
    checkUpper = password[upper]

    if value == checkLower and value == checkUpper:
        return False
    elif value == checkLower or value == checkUpper:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Total passwords meeting policy #1 : {}".format(selectOption(1)))
    print("Total passwords meeting policy #2 : {}".format(selectOption(2)))
