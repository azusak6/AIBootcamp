# Kiểm tra số nhập vào có phải số nguyên tố hay không

num = int(input("Enter a number: ")) # Xuất ra ngoài màn hình Enter a number: -> sau đó cho phép nhập num trên cùng dòng

'''
print("Enter a number: ") # Xuất ra ngoài màn hình Enter a number: rồi xuống dòng
num = int(input()) # nhập num với kiểu dữ liệu Integer - int
'''

# a ** b: được hiểu là a mũ b
# a ** 0.5 được hiểu là a mũ 1/2, tức là căn bậc 2 của a

'''
a = 12345
print(f'gia tri cua a la {a}') # xuat ra: gia tri cua a la 12345

# Tương đương với cách dưới đây:
a = 12345
print('gia tri cua a la ', a)
'''

if num > 1:
    for i in range(2, int(num**0.5) + 1): # i chạy từ 2 đến giá trị nguyên của căn bậc 2 của num + 1
        if num % i == 0:
            print(f"{num} is not a prime number")
            break # Thoát khỏi vòng lặp, không kiểm tra các giá trị của i ở phía sau nữa vì num đã không thỏa mã điều kiện của số nguyên tố
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number") # num < 1 nên sẽ không kiểm tra và chắc chắn không là số nguyên tố