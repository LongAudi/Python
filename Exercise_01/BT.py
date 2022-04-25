#1
# String = "nGuYen vAn a"
# print(String.title())

#2
# chuoi = ['lap' 'trinh' 'bang' 'ngon' 'ngu' 'python']
# chuoi.reverse()
# print(chuoi)

#3
# a = [1,2,2,3,3,3,4,4,4,4]
# b = []
# c= []
# for i in range(len(a)-1): 
#     b.append(a.count(a[i]))

# for i in range(len(b)-1):
#     if b[i] == max(b):
#         c.append(a[i])

# print('gia tri xuat hien nhieu nhat = ',c[0])

# 4
# string = input(">>")
# count={}
# for i in string:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i] = 1
 
# print(count)

#5
# import re
# s = 'long 146'

# m = re.findall(r'\d', s)
# r = ' '.join(m)

# l = re.split(r'\d', s)
# h = ' '.join(l)

# print(r)
# print(h)

#6
# name = input("nhap vao ho ten: ")

# print(name.split(" ",2))

#7
# String = input("Nhập vào chuỗi: ")
# print(String.title())

#8
# name = 'ABCDEfgh'

# print(''.join([char.upper() if i%2==0 else char.lower() for i, char in enumerate(name)]))

#9
# def num(n): 

#     flag =0;
#     if ( n[::-1] == n):
#       flag = 1
#     return flag

# n = input(">> Nhập vào một số: ")
# check = num(n);
 
# if check == 1:
#     print(n,"là số đối xứng")
# else:
#     print(n,"không phải là số đối xứng")

#10
n=int(input('nhập số có 3 chữ số: '))
def docso(so):
    donvi=('','một ','hai ','ba ','bốn ','năm ','sáu ','bảy ','tám ','chín ','mười ','mười một ','mười hai ','mười ba ','mười bốn ','mười lăm ','mười sáu ','mười bảy ','mười tám ','mười chín ')
    hangchuc=('','','hai mươi ','ba mươi ','bốn mươi ','năm mươi ','sáu mươi ','bảy mươi ','tám mươi ','chín mươi ')
    if so<0:
        return "âm " +docso(-so)
    if so<20:
        return  donvi[so]
    if so<100:
        return  hangchuc[so//10] + donvi[int(so % 10)]
    if so<1000:
        return donvi[so // 100]  +"trăm " + docso(int(so % 100))
print(docso(n))