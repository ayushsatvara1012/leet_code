from itertools import combinations, permutations

def letter_combination_of_number(s_digits):
    """find the combinations of the char in the phone number """
    all_chars = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }
    for i in s_digits:
        for j in s_digits[i]:


print(letter_combination_of_number('23'))