# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
total_groups = int(input())
final = dict.fromkeys(groups)
for a, b in zip(range(total_groups), groups):
    final[b] = int(input())

print(final)