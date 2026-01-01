print("Number System Conversion")
print("1. Decimal to Binary")
print("2. Decimal to Octal")
print("3. Decimal to Hexadecimal")
print("4. Binary to Decimal")
print("5. Octal to Decimal")
print("6. Hexadecimal to Decimal")

ch = int(input("Enter your choice: "))


if ch == 1:
    n = int(input("Enter decimal number: "))
    binary = ""
    while n > 0:
        r = n % 2
        binary = str(r) + binary
        n = n // 2
    print("Binary:", binary)


elif ch == 2:
    n = int(input("Enter decimal number: "))
    octal = ""
    while n > 0:
        r = n % 8
        octal = str(r) + octal
        n = n // 8
    print("Octal:", octal)


elif ch == 3:
    n = int(input("Enter decimal number: "))
    hexa = ""
    while n > 0:
        r = n % 16
        if r < 10:
            hexa = str(r) + hexa
        else:
            hexa = chr(r + 55) + hexa
        n = n // 16
    print("Hexadecimal:", hexa)


elif ch == 4:
    b = input("Enter binary number: ")
    decimal = 0
    power = 0
    i = len(b) - 1
    while i >= 0:
        decimal = decimal + int(b[i]) * (2 ** power)
        power = power + 1
        i = i - 1
    print("Decimal:", decimal)


elif ch == 5:
    o = input("Enter octal number: ")
    decimal = 0
    power = 0
    i = len(o) - 1
    while i >= 0:
        decimal = decimal + int(o[i]) * (8 ** power)
        power = power + 1
        i = i - 1
    print("Decimal:", decimal)


elif ch == 6:
    h = input("Enter hexadecimal number: ")
    decimal = 0
    power = 0
    i = len(h) - 1
    while i >= 0:
        if h[i] >= '0' and h[i] <= '9':
            value = ord(h[i]) - 48
        else:
            value = ord(h[i]) - 55
        decimal = decimal + value * (16 ** power)y ñ
        power = power + 1
        i = i - 1
    print("Decimal:", decimal)

else:
    print("Invalid choice")
