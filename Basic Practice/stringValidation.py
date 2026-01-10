if __name__ == '__main__':
    s = input()
    print(any(s.isalnum() for s in s))
    print(any(s.isalpha() for s in s))
    print(any(s.isdigit() for s in s))
    print(any(s.islower() for s in s))
    print(any(s.isupper() for s in s))

