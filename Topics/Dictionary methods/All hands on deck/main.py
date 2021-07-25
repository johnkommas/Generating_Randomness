
cards = []
for i in range(6):
    x = input()
    if x.lower() == 'jack':
        cards.append(11)
    elif x.lower() == 'queen':
        cards.append(12)
    elif x.lower() == 'king':
        cards.append(13)
    elif x.lower() == 'ace':
        cards.append(14)
    elif x.isdigit():
        cards.append(int(x))

print(sum(cards) / len(cards))
