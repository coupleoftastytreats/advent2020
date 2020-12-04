
def countValid(validate="no"):
    totalvalid = 0
    data = open("day4.txt").readlines()
    for n, line in enumerate(data):
        if line.startswith("\n"):
            data[n] = "\n"+line.rstrip()
        else:
            data[n] = line.rstrip()
    entry = '|'.join(data)  # Fixes this list
    x = entry.split("\n")  # Re split based on new \n delimiter
    for new_entry in x: # Change this back to x when done
        if validatePassport(new_entry, validate) == "valid":
            totalvalid += 1
    return totalvalid


def validatePassport(entry,validate):
    total_count = 0
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for item in valid_fields:
        if item in entry:
            #print("Valid Item! {}".format(item))
            total_count += 1
        else:
            pass

    # If 7+ correct fields, its valid
    if total_count >= 7:
        if validate == "no":
        #print("Valid Entry {}".format(entry))
            return "valid"
        #print("Sending entry to validator:")
        if validate == "yes":
            if validateFields(entry):
                return "valid"
    else:
        #print("Invalid Entry {}".format(entry))
        return "invalid"


def byr(x):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    #print("evaluating byr {}".format(x))
    if 1920 <= int(x) <= 2002:
        #print("[+] BRY Passed {}".format(x))
        return True


def iyr(x):
    #    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    #print("evaluating iyr {}".format(x))
    if 2010 <= int(x) <=2020:
        #print("[+] IYR Passed {}".format(x))
        return True


def eyr(x):
    #    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    #print("evaluating eyr {}".format(x))
    if 2020 <= int(x) <= 2030:
        #print("[+] EYR Passed {}".format(x))
        return True


def hgt(x):
    #    hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76
    #print("evaluating hgt {}".format(x))
    if "cm" in x:
        x = x.strip("cm")
        if 150 <= int(x) <= 193:
            #print("[+] HGT Passed {}".format(x))
            return True
    elif "in" in x:
        x = x.strip("in")
        if 59 <= int(x) <= 76:
            #print("[+] HGT Passed {}".format(x))
            return True


def hcl(x):
    #     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    #print("evaluating hcl {}".format(x))
    if "#" in x:
        if len(x) == 7:
            #print("[+] HCL Passed {}".format(x))
            return True


def ecl(x):
    #     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    #print("evaluating ecl {}".format(x))
    eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for color in eye:
        if color in x:
            #print("[+] ECL Passed {}".format(x))
            return True


def pid(x):
    #     pid (Passport ID) - a nine-digit number, including leading zeroes.
    #print("evaluating pid {}".format(x))
    if len(x) == 9:
        #print("[+] PID Passed {}".format(x))
        return True


def evalFields(case, val):

    if case == "byr":
        return(byr(val))

    if case == "iyr":
        return(iyr(val))

    if case == "eyr":
        return(eyr(val))

    if case == "hgt":
        return(hgt(val))

    if case == "hcl":
        return(hcl(val))

    if case == "ecl":
        return(ecl(val))

    if case == "pid":
        return(pid(val))


def validateFields(entry):
    total_count = 0
    entry = entry.replace("|", " ")
    criteria = entry.split(" ") # Breaks each entry in spaces
    # Create a dictionary with key pairs
    categories = []
    values = []

    for i in criteria:
        try:
            check = i.split(":")
            cat = check[0]
            val = check[1]
            categories.append(cat)
            values.append(val)
        except:
            pass

    dict_of_passport_properties = dict(zip(categories,values))
    valid_count = 0
    for key in dict_of_passport_properties:
         if evalFields(key, dict_of_passport_properties[key]):
             valid_count += 1

    if valid_count >= 7:
        return True

if __name__ == '__main__':
    print("Part 1, Total Valid Passports = {}".format(str(countValid())))  # 196
    print("Part 2, Verifying Passport Data = {}".format(str(countValid(validate="yes"))))  # 114
    