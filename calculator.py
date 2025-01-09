def binary_calculator(bin1, bin2, operator):
    number = 0
    number2 = 0
    total = 0

 

    
    # converts bin1 to decimal
    for place, digit in enumerate(bin1[::-1]):
        if digit != '1' and digit != '0':
            return 'Error'
        if digit == '1':
            number += 2 ** place
    
    # converts bin2 to decimal
    for place2, digit2 in enumerate(bin2[::-1]):
        if digit2 != '1' and digit2 != '0':
            return 'Error'
        if digit2 == '1':
            number2 += 2 ** place2

    # operations
    if operator == '+':
        total = int(number) + int(number2)
    
    elif operator == '-':
        total = int(number) - int(number2)
    
    elif operator == '/':
        # checks to see is the divisor is 0. if it is then it will return 'NaN'
        if number2 == 0:
            return "NaN"
        else:
            total = int(number) / int(number2)
    
    elif operator == '*':
        total = int(number) * int(number2)

    # makes sure that the decimal stays in 8 bit, with the max number it can go to is 255. If the number is negative or over 255, it will return 'Overflow'
    if total > 255 or total < 0:
        return 'Overflow'
    
    # converts the decimal back in binary
    powers = [128, 64, 32, 16, 8, 4, 2, 1]
    end = ''
    for power in powers:
        if total >= power:
            end += '1'
            total -= power
        else:
            end += '0'
    
    return end
            

       
print(binary_calculator("1010", "1010", "+"))  # Should return "00010100"
print(binary_calculator("1100", "0011", "-"))  # Should return "00001001"
print(binary_calculator("1010", "0000", "/"))  # Should return "NaN"
print(binary_calculator("1010", "abc", "+"))   # Should return "Error"
print(binary_calculator("11111111", "00000001", "+"))  # Should return "Overflow"
print(binary_calculator('011','110', '-'))
