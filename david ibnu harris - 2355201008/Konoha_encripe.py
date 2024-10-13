def decryptEligma(x):
    total_shift = 0
    decryptPesan = []

    for char in x:
        if char.isdigit():
            total_shift += int(char)
        elif char.isalpha():
            decryptPesan.append(char)
    

    for i in range(len(decryptPesan)):
        original_char = decryptPesan[i]
        
        if original_char.islower():
            shifted_char = chr((ord(original_char) - ord('a') + total_shift) % 26 + ord('a'))
        else:
            shifted_char = chr((ord(original_char) - ord('A') + total_shift) % 26 + ord('A'))
        
        decryptPesan[i] = shifted_char


    return ''.join(decryptPesan)

x = input("Enter Code: ")
output = decryptEligma(x)
print(output)  
