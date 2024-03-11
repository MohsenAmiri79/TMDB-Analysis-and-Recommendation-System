def multiline_print(lst, width=5):
    for i in range(0, len(lst), width):
        row = lst[i:i+width]
        formatted_row = ' | '.join(map(str, row))
        print(f'| {formatted_row} |')
    print("")
