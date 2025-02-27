sum = 0
for _ in range(1000):
    num = int(input("Enter numbers (-1 or 999 to stop): "))
    
    if num == -1 or num == 999:
        break  
    
    sum += num  

print(f"Sum of entered numbers: {sum}")
