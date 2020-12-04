
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID) - Doesn't need to be there

VALID = Has all 8 fields
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

INVALID = Missing HGT field
iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

"""

"""
Opt 1
1. Read input into a dictionary with keys
2. If no entry for key, mark invalid

Opt 2
1. re.search for each key in each entry"""


import re
import os

def countValid():
    totalvalid = 0
    data = open("day4.txt").readlines()
    for n, line in enumerate(data):
        if line.startswith("\n"):
            data[n] = "\n"+line.rstrip()
        else:
            data[n] = line.rstrip()
    entry = '|'.join(data)  # Fixes this list
    x = entry.split("\n")  # Re split based on new \n delimiter
    for new_entry in x:
        if validatePassport(new_entry) == "valid":
            totalvalid += 1
    return totalvalid


def validatePassport(entry):
    total_count = 0
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    #valid_fields = ["hcl", "ecl"]

    for item in valid_fields:
        if item in entry:
            #print("Valid Item! {}".format(item))
            total_count += 1
        else:
            pass

    # If 7+ correct fields, its valid
    if total_count >= 7:
        print("Valid Entry {}".format(entry))
        return "valid"
    else:
        #print("Invalid Entry {}".format(entry))
        return "invalid"
    #print(total_count)


if __name__ == '__main__':
    print("Part 1, Total Valid Passports = {}".format(str(countValid())))