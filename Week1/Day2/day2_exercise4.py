# Tìm số lớn nhất trong danh sách cho trước bằng cách sử dụng vòng lặp for

List = [7, 2, 3, 1, [11, 20], 10, [14, 15, 0]]

# Khái niệm danh sách (list) lồng nhau:
'''
a = [1 , 6, 8, 0, 4] # list bình thường
b = [7, 5, [3, 9], 6] # list lồng nhau

# ở trong danh sách a ta có: a[0] = 1, a[1] = 6, a[2] = 8, a[3] = 0, a[4] = 4

# ở trong danh sách b ta có: b[0] = 7, b[1] = 5, b[2][0] = 3, b[2][1] = 9, b[3] = 6
print(b[2][0]) # Output: 3
'''

# len(A) : Hàm tìm kích thước của mảng, chuỗi - xâu ,danh sách, tuple A
# type(A) : Kiểm tra kiểu dữ liệu mà đang được dùng cho A

Max = -9999999999999999999999999

for i in range(0, len(List)): # i chạy từ 0 đến giá trị cuối cùng của danh sách List 
    # print(List[i]) # xuat ra từng giá trị môt roi xuong dong
    '''
    # Output:
    7
    2
    3
    1
    [11, 20]
    10
    [14, 15, 0]

    '''

    if( type(List[i]) != list ): # Kiểu dữ liệu của biến tại vị trí i không thuộc loại list
        if(List[i] > Max): Max = List[i]

    else: # Nếu như Kiểu dữ liệu của biến List[i] thuộc loại list thì ta sẽ so sánh với từng giá trị List[i][j]
        for j in List[i]:
            if(j > Max): Max = j

print(f'Max = {Max}')
    
