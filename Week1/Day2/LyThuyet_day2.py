# Lưu ý: chạy thử từng đoạn code một để hiểu
# print(A): Xuất xong giá trị A rồi xuống dòng
# print(A, B): Xuất xong giá trị A và B rồi xuống dòng
# '\n' là kí tự xuống dòng
# print(A, '\n', B): Xuất xong A rồi xuống dòng sau đó xuất ra B rồi xuống dòng tiếp 
#---------------------------------------------------------------------------------------------------------------------------------------------

# Syntax for for-loop
'''
for item in sequence:
    # Code block
'''

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



# Loop with range
for i in range(5): # [0,1,2,3,4] 
    print(i)



for j in range(1, 5): # [1, 2, 3, 4]
    print("j = ", j)

#---------------------------------------------------------------------------------------------------------------------------------------------


# Syntax for while-loop
'''
while condition:
    # Code block
'''

#count down from 5 - đếm ngược từ 5
count = 5
while count > 0:
    print(count)
    count -= 1 # count = count - 1

print("Outside While Loop")




#---------------------------------------------------------------------------------------------------------------------------------------------

# break - continued
for i in range(10):
    if i == 5: # Nếu i = 5 thì sẽ thoát khỏi vòng lặp
        break
    print(i) # Nếu i < 5 thì sẽ thực hiện lệnh này

print("Outside For Loop")




for i in range(10):
    if i == 7: # Nếu i == 7 thì sẽ nhảy đến bước tiếp theo - không xuất ra 7
        continue
    print(i)

print("Outside For Loop")




for i in range(10):
    if i % 2 == 0: 
        continue
    print(i) 


#---------------------------------------------------------------------------------------------------------------------------------------------

#if-elif-else 

# Example 1: checking a condition
num = -50
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else: 
    print("Negative Number")



# Example 2: Nested conditions - Điều kiện lồng nhau
age = 25
if age > 10:
    if age < 30: 
        print("Young Adult")
    else:
        print("Adult")
