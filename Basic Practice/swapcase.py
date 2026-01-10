# Que: Swap the case of the string
# ? input - pYtHon ProGRAmmiNG
# ? output - PyThON pROgraMMIng

def swap_case(strName):
    return ''.join([item.lower() if item.isupper() else item.upper() for item in strName])

if __name__ == '__main__':
    strName = input()
    print(swap_case(strName))



