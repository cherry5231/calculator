print("Welcome to basic calculator")
print("""enter exp if you want to raise a number to a power\n
enter sqrt if you want square root of a number\n
enter add if you want to add two numbers\n
enter sub if you want to subtract two numbers\n
enter mul if you want to multiply two numbers\n
enter div if you want to divide two numbers\n
enter mod if you want to find the modulus of two numbers\n
     """)
choose = input("Enter your choice: ")
if choose == "exp":
    num = int(input("Enter the number: "))
    power = int(input("Enter the power: "))
    print(num**power)

elif choose == "sqrt":
    num = int(input("Enter the number: "))
    print(num**0.5)
elif choose == "add":
    count = int(input("how many numbers do you want to add? "))
    
    total = 0
    for i in range(count):
        num = int(input("Enter the number: "))
        total = total + num
   
       
    print(total)
elif choose == "sub":
    count = int(input("how many numbers do you want to sub? "))
    
    total = int(input("Enter the first number: "))
    for i in range(count-1):
        num = int(input("Enter the remaining numbers: "))
        total = total - num
    print(total)
elif choose == "mul":
    count = int(input("how many numbers do you want to multiply? "))
    
    total = 1
    for i in range(count):
        num = int(input("Enter the number: "))
        total = total * num
    print(total)
elif choose == "div":
    count = int(input("how many numbers do you want to divide? "))
    
    total = float(input("Enter the first number: "))
    for i in range(count-1):
        num = float(input("Enter the remaining numbers: "))
        total = total / num
    print(total)
elif choose == "mod":
    count = int(input("how many numbers do you want to find the modulus of? "))
    
    total = float(input("Enter the first number: "))
    for i in range(count-1):
        num = float(input("Enter the remaining numbers: "))
        total = total % num
    print(total)
else:
    print("Invalid choice")