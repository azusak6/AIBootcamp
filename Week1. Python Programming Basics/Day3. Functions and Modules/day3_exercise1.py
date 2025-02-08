# Create a Function to Calucate Factorials - Viết hàm tính giai thừa

def factorial(n):
    if n == 1: 
        return n # hoac return 1
    else:
        return n * factorial(n-1)
    
def print_factorial(n):
    print("n! = ", factorial(n))

n = int(input("Enter your number:"))
print_factorial(n)

