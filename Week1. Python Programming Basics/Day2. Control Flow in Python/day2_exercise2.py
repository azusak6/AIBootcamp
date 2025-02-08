# Tạo một máy tính điều khiển menu (Create a Menu-Driven Calucator)

def add(a, b): # Viết hàm tính tổng (function - chương trình con tính tổng)
    return a + b # Trả về giá trị a + b

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else: return "Division by zero is not allowed"


while True:
    print("\nMenu:") # '\n' là kí tự xuống dòng
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multipliation")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting Program.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result: ", add(num1, num2)) 
        '''
        # Tương đương với:
        print(f'Result: {add(num1, num2)}') 
        '''
        # add(num1, num2) nghĩa là ta sử dụng hàm add(a,b) ở bên trên với a = num1 và b = num2
        # Câu lệnh return a + b ở hàm add là trả về giá trị của num1 + num2
        '''
        # Tương đương với:
        res = add(num1, num2)
        print("Result: ", res) # hay print(f'Result: {res}') 
        '''
    
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2)) 
    else :
        print("Result: ", divide(num1, num2)) 
    

# elif  có thể viết là else if