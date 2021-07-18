import json
# The following lines create dictionaries from the input. Do not modify them, please
#auto check
first_family = json.loads(input())
second_family = json.loads(input())

# #manual check
# first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}
# second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard", "husband's sister": "Isabelle"}
# Work with the 'first_family' and 'second_family' and create a new dictionary
# making a new dictionary

whole_family = {}
whole_family.update(first_family)
whole_family.update(second_family)
print(whole_family)
