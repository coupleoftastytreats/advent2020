

boarding_passes = open("day5.txt", 'r').readlines()

#print(boarding_passes)

# Multiply row * 8 and add column for seat ID
#sample = "BFFFBBFRRR" # row 70, column 7, seat ID 567
#sample = "FFFBBBFRRR"
#sample = "FBFBBFFRLR"
#print(boarding_passes[0])

def collectTickets():
    total = []
    for entry in boarding_passes:
        #determineSeat(entry)
        total.append(determineSeat(entry))

    print(total)
    print(len(total))
    print(max(total))
    #903 too high?

def determineSeat(pass_entry):
    lower_row = 1
    upper_row = 128
    divider = (upper_row - lower_row) / 2
    row = 0
    lower_col = 1
    upper_col = 8
    col_div = (upper_col - lower_col) / 2
    column = 0
    for half in pass_entry:
        if half == "F":
            lower_row = int(lower_row)
            upper_row = int(upper_row - divider)
            divider = (upper_row - lower_row)/2
            #print("F", lower_row, upper_row, divider)
            row = lower_row

        if half == "B":
            lower_row = int(upper_row - divider)
            upper_row = int(upper_row)
            divider = (upper_row - lower_row)/2
            #print("B", lower_row, upper_row, divider)
            row = upper_row

        if half == "L":
            lower_col = int(lower_col)
            upper_col = int((upper_col - col_div))
            col_div = (upper_col - lower_col)/2
            #print("L", lower_col, upper_col, col_div)
            column = int(lower_col)
        if half == "R":
            lower_col = int((upper_col - col_div))
            upper_col = int(upper_col)
            col_div = (upper_col - lower_col)/2
            #print("R", lower_col-1, upper_col-1, col_div)
            column = int(upper_col-1)
    seat_id = (row * 8) + column
    print("[+] Ticket {} = Row {} Column {} Seat ID {}".format(pass_entry,row, column, seat_id))
    return seat_id


if __name__ == '__main__':
    collectTickets()
    #print(determineSeat("FBFBBFFRLR"))