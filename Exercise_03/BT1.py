def check_SNT(n):
    flag = True
 
    # Kiểm tra SNT
    if (n < 2):
        flag = False
    elif (n == 2):
        flag = True
    elif (n % 2 == 0):
        flag = False
    else:
        for i in range(3, n, 2):
            if (n % i == 0):
                flag = False
    return flag

tong = 0
 
for i in range(10):
    if (check_SNT(i)):
        print(i,end=' + ')
        tong += i
print(" = ", tong)