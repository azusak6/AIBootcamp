# Viết chương trình tính giai thừa của một số bằng hàm 

def giaithua(n):
    if n == 1: 
        return n
    else:
        return n * giaithua(n-1)
    
n = int(input("Enter your number: "))
print(f'n! = {giaithua(n)}')