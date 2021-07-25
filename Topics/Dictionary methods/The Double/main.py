# put your python code here
import string
alphabet = string.ascii_lowercase
double_alphabet = {}
for letter in alphabet:
    double_alphabet[letter] = f'{letter * 2}'

# print(double_alphabet)