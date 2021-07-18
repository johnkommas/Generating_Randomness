# put your code here
from statistics import mean

final = []
while True:
    x = int(input())
    if x == 55:
        break
    else:
        final.append(x)

print(len(final))
print(sum(final))
print(round(mean(final)))
