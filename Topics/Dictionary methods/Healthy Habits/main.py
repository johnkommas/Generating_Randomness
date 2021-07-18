# the list "walks" is already defined

# your code here
result = 0
for walk in walks:
    result += walk['distance']
print(result // len(walks))