def split_and_join(line):
    newLine = line.split(' ')
    newstring = '-'.join(newLine)
    return newstring

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)