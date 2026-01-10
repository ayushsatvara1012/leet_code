import textwrap

def wrap(s,txtwrp):
    return textwrap.fill(s,txtwrp)
if __name__ == '__main__':
    s = str(input())
    txtwrp = int(input())
    print(wrap(s,txtwrp))