import numpy as np
number_a = int(input())
number_b = int(input())
lst = []
for i in range(number_a, number_b+1):
    if i % 3 == 0:
        lst.append(i)
print(np.mean(lst))
