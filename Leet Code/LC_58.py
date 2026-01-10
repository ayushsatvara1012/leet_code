def lenOfLastWord(s):
    lst_word = list(s.strip().split(' '))
    return len(lst_word[-1])
print(lenOfLastWord('Hello world i am python learner '))