def addBinary(a,b):
    add_decimal = int(a,2)+int(b,2)
    binary_dec = bin(add_decimal)[2:]
    return binary_dec
print(addBinary('11','1'))