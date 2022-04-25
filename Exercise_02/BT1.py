from math import sqrt

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số cuối cùng: "))

if a > b:
    print("Số thứ nhất lớn hơn số thứ 2!")
else:
    for i in range(a,b+1):
        if i % 2 == 0 and sqrt(i) %2!=0:
            print(i)