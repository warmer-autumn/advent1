def line_input():
    read = open('input.txt', 'r')
    read = read.read()
    read = read.splitlines()
    return read

def compare(total, past_total):
    if total > past_total:
        past_total = total
        total = past_total
    return total

def get_calories(input):
    number = input
    total = 0
    past_total = 0
    for line in input:
        current_line=int(line)
        print(f'current line is: {current_line}')
        if current_line != 0:
            total+=current_line
            print('total is now: '+ str(total))
        else: 
            compare(total, past_total)
    return total
