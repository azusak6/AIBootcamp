# Function - Hàm (Chương trình con) là gì
'''
+ Khối mã tái hiện một nhiệm vụ cụ thể 
+ Có thể tái sử dụng
+ Nếu nhiều câu lệnh cùng thực hiện một hành động giống nhau thì ta có thể sử dụng function để thực hiện
+ Hàm bắt đầu bằng từ khóa def
'''

# Syntax
'''
def function_name(paranameters):
    #Code block
    return result
'''

# Example: Function with paranameters and return value
def add_numbers(a, b):
    return a + b
    # Hoặc
    '''
    c = a + b
    return c
    '''

result = add_numbers(5, 3) # gọi hàm add_number cho 5 và 3; gan 5 cho a, 3 cho b
print("Sum: ", result)
print("Sum_1: ", add_numbers(5,3))

#Lưu ý: Nếu ta thay giá trị của dòng 18: 
'''
thay vì return a + b thì ta có thể thay bằng một giá trị khác nhưng phải xác định:
    ví dụ 1: 3 + a, 4 + 100, 5 + b, ...
    và khi thực hiện chuong trình ta có thể bỏ a, b trong ngoặc ở dòng 17 đi vì không quan trọng khi ta làm theo ví dụ 1 trên
    nghĩa là khi ta return a + 3 chẳng hạn thì ta có thể bỏ b trong dòng 17 đi và khi gọi ham 
'''




#-------------------------------------------------------------------------------------------------------------------------------------------------------------



# Scope and Lifetime of Variable - Phạm vi của biến trong suất chương trình

# Scope
'''
- Local Scope: Phạm vi cục bộ
    + Các biến được khai báo, xác định ở bên trong các hàm, các khối mã và chỉ có thể truy cập được trong khi thực hiện các hàm, khối mã chứa nó

- Global Scope: Phạm vi toàn cụ 
    + Các biến được khai báo, xác định ở bên ngoài các hàm, các khối mã và có thể truy cập được trong suất thời gian thực hiện chương trình
'''

# Example: 
a, b = 5, 6 # khai báo hai biến a, b và gán 5 cho a, 6 cho b
message = a + b # Global Variable

def greet():
    message = "Hello World!" # Local Variable
    print(message)

greet() # Gọi hàm greet()
print("a + b = ", message)

message += 10 # Global Variable
print("message = ", message)




#-------------------------------------------------------------------------------------------------------------------------------------------------------------


# Nhập và sử dụn các Modules
'''
Modules là các tệp Python chứa tập hợp các hàm có sẵn trong Python và biến có thể sử dụng lại.
Ví dụ: Modules toán học: math()
'''



# Cách sử dụng hàm có sẵn trong Modules - Cách 1: 
# Khai báo sử dụng thư viện module (mô-đun) toán học
'''
import math #Khai báo sử dụng thư viện module (mô-đun) toán học
Module.function()
'''
import math
print(math.sqrt(16))  # sử dụng hàm căn bậc 2 sqrt() của mô-đun math để tính căn bậc 2 của 16 sau đó in ra kết quả và xuống dòng





# Cách sử dụng mô-đun khác - Cách 2:
'''
frome Module import function
function()
'''
from math import sqrt #Khai báo sử dụng thư viện module (mô-đun) toán học và gọi hàm sqrt
print(sqrt(16)) # sử dụng hàm căn bậc 2 sqrt() của mô-đun math để tính căn bậc 2 của 16 sau đó in ra kết quả và xuống dòng




# Cách 3 - Sử dụn mô-đun bằng cách đặt tên khác cho function được gọi ra:
'''
frome Module as XName
XName.function()
'''
import math as m # định nghĩa m chính là tên khác của math - chức năng như math
print(m.sqrt(16))



#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tạo các Module của riêng mình (Tìm hiểu kĩ hơn ở phần sau)

'''
Tạo file module có tên bất kì, ví dụ: Modules_TEST.py được lưu trong thư mục: Modules
Tạo file code Python để sử dụng các mô-đun được viết trong file Modules_TEST.py, ví dụ: Test_Modules.py được lưu trong thư mục Modules
'''

# Trong file Modules_TEST.py
def giaithua(n):
    if n == 1:
        return n
    else: return n * giaithua(n-1)


# Trong file Test_Modules.py
import Modules_TEST
n = 5
print(Modules_TEST.giaithua(n))
