from datetime import datetime
import io
from itertools import count

import re

import regex

with open ('./Exercise_04/Input.txt','r',encoding='utf8') as fileinp:
    count = 1
    x = input("Nhập điều kiện cần tìm: ")
    datalist = fileinp.readlines()
    for line2 in datalist:
        if x in line2:
            print(str(count)+" "+str(line2))
            count +=1

# Địa chỉ 
# with open('./Exercise_04/Output_DiaChi.txt','w',encoding='utf8') as fileout:
#     count = 1
#     for line2 in datalist:
#         if x in line2:
#             i = re.sub('Địa chỉ: ','',line2)
#             y = re.sub('Huyện','H.',str(i))
#             z = re.sub('Thành phố','TP.',str(y))
#             h = re.sub('Quận', 'Q.',str(z))
#             fileout.write(str(count)+"-"+str(h))
#             count +=1

# Mã số thuế
# with open('./Exercise_04/Output_MaSoThue.txt','w',encoding='utf8') as fileout:
#     count = 1
#     for line2 in datalist:
#         if x in line2:
#             i = re.sub('Mã số thuế: ','',line2)
#             fileout.write(str(count)+"-"+str(i))
#             count +=1

# Ngành nghề chính
# with open('./Exercise_04/Output_NganhNgheChinh.txt','w',encoding='utf8') as fileout:
#     count = 1
#     for line2 in datalist:
#         if x in line2:
#             i = re.sub('Ngành nghề chính: ','',line2)
#             fileout.write(str(count)+"-"+str(i))
#             count +=1

# Ngày thành lập
with open('./Exercise_04/Output_NgayThanhLap.txt','w',encoding='utf8') as fileout:
    count = 1
    for line2 in datalist:
        if x in line2:
            i = re.sub('Ngày thành lập: ','',line2).replace(":","").strip()
            z = datetime.strptime(i,"%d-%m-%Y").strftime("%y%m%d")
            y = re.sub('-','',str(z))
            fileout.write(str(count)+"-"+str(y)+"\n")
            count +=1