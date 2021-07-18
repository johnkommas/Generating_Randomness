string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiouy'
count = 0

# fix this for loop
for i in range(len(string)):
    if string[i] in vowels:
        count += 1
