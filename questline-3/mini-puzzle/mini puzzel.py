binary_str = input("Enter a binary string : ")
k = int(input("Enter how many steps you wanna rotate : "))
n = len(binary_str)
k = k % n 
direction = "left"
if direction == "left":
    rotated = binary_str[k:] + binary_str[:k]
else:
    rotated = binary_str[-k:] + binary_str[:-k]
print(int(rotated, 2))  
