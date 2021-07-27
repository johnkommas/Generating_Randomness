numbers = [int(number) for number in input()]
x = []
for i, number in enumerate(numbers):
    if i != 0:
        x.append(number + x[i - 1])
    else:
        x.append(number)
print(x)
