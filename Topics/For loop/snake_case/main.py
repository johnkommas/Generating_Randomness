noob_input = input()
pro_output = ''
for noob in noob_input:
    if noob == noob.upper():
        pro_output += f'_{noob.lower()}'
    else:
        pro_output +=noob

print(pro_output)
