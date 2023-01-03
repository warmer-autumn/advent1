def line_input():
    read = open('test_input.txt', 'r')
    read = read.read()
    read = read.splitlines()
    return read

def compare(total, past_total):
    top_total=0
    if total >= past_total:
        print(f'{total} is greater than {past_total}')
        top_total = total
        past_total = total
        return
    else:
        print(f'{total} is less than {past_total}')
        return top_total

def get_calories(input):
    number = input
    total = 0
    past_total = 0
    top_total=0
    for line in input:
        current_line=line
        print(f'current line is: {current_line}')
        if current_line != '':
            total+=int(current_line)
            print('new total is now: '+ str(total))
        else: 
            print(f'comparing new total: {total} vs past total: {past_total}:')
            compare(total, past_total)
            print(f'the result is {top_total}')
    return top_total
