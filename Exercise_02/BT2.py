import random
from datetime import datetime
import datetime

now = datetime.datetime.now()
x = int(now.microsecond) // 1000
# print('%s' % (now.microsecond))

the_number = random.randint(1,999)
count = 0
while count < int(now.microsecond) //1000:
    count +=1
    the_number = int(input("Mời bạn chọn số từ 1 - 999: "))
    if x==the_number:
        print('Ban da du doan chinh xac so: ',x)
        break
    if x>the_number:
        print('So nho qua!')
        print(f'ban tra loi sai {count} lan')
    if x<the_number:
        print('So lon qua')
        print(f'ban tra loi sai {count} lan')
print("Đáp án là: ",x)
print("Tổng số lần sai: ",count)