number_a = int(input())
lst = []
for i in range(number_a):
    lst.append(int(input()))

for i in lst:
    if i % 7 == 0:
        print(i**2)
