
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

output = []
get_input()