def print_as_table(lst, width):
    for i in range(0, len(lst), width):
        row = lst[i:i+width]
        formatted_row = ' | '.join(map(str, row))
        print(f'| {formatted_row} |')
    print("")
