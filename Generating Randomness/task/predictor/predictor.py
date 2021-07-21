def get_input():
    print("Print a random string containing 0 or 1: \n")
    data = input()
    for letter in data:
        if letter in ['0', '1']:
            output.append(letter)
    if len(output) < 100:
        print(f'Current data length is {len(output)}, {100 - len(output)} symbols left')
        return get_input()
    print(f"Final data string:\n{''.join(output)}")
    return ''.join(output)


def profile(info):
    triads = ["000", "001", "010", "011", "100", "101", "110", "111"]
    dict_of_triads = {}
    dict_of_zeros = dict_of_triads.fromkeys(triads, 0)
    dict_of_ones = dict_of_triads.fromkeys(triads, 0)
    for i in range(len(info) - 3):
        triad = info[i:i + 3]
        if info[i + 3] == '0':
            dict_of_zeros[triad] += 1
        elif info[i + 3] == '1':
            dict_of_ones[triad] += 1
    for key in dict_of_zeros:
        print(f"{key}: {dict_of_zeros[key]},{dict_of_ones[key]}")


output = []
profile(get_input())


