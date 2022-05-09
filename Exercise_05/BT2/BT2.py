import pandas as pd
import os
from pandas import ExcelWriter
from pandas import ExcelFile

df1 = os.path.dirname(os.path.realpath(__file__))
def Outfile(old_path, new_location):
    import datetime
    h = datetime.datetime.now()
    name = old_path.split("\\")[-1]
    new_path = new_location + "\\" + name
    if os.path.exists(old_path):
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
        elif os.path.exists(new_path):
            new_path = new_location + "\\" + \
            "(" +str(h).split('.')[0].replace(':','') + ") " + name
        os.rename(old_path, new_path)
    return

Outfile(df1+'\\Output\\output.xlsx',df1+'\\Output\\bak')

dfInput = pd.read_excel(df1 +'\\input\\Input.xlsx',sheet_name= 0,header=1)
dfMaster = pd.read_excel(df1 + '\\Master.xlsx',sheet_name= 0)
for j in range(len(dfInput)):
    dfMasterTemp = dfMaster.loc[dfMaster['Mã số thuế'] == dfInput.loc[j,'MST đơn vị mua hàng']]
    print(dfMasterTemp)
    if len(dfMasterTemp) > 0:
        dfInput.loc[j,'Họ tên người mua hàng'] = str(dfMasterTemp.iloc[0]['Tên khách hàng (*)'])
countSheet = 0
countLenHD = 0
countSoHD = 0
dfOutput = dfInput[0:0]
writer = pd.ExcelWriter(df1 +'\\Output\\output.xlsx')
for i in range(len(dfInput)-1):
    dfOutput.loc[i] = dfInput.loc[i]
    dfOutput.to_excel(writer, sheet_name='Sheet'+str(countSheet),index=False)
    if dfInput.loc[i, 'Số HĐ'] != dfInput.loc[i+1,'Số HĐ']:
        countSoHD +=1
    if countSoHD%3==0 and countSoHD !=0:
        intSoHD = countSoHD
        countSoHD = 0
        countSheet +=1
        dfOutput = dfInput[0:0]
    countLenHD +=1
if dfInput.loc[countLenHD-1,'Số HĐ'] != dfInput.loc[countLenHD,'Số HĐ'] and intSoHD%3!=0:
    dfOutput.loc[countLenHD] = dfInput.loc[countLenHD]
elif dfInput.loc[countLenHD-1,'Số HĐ'] == dfInput.loc[countLenHD,'Số HĐ'] and intSoHD%3==0:
    dfOutput.loc[countLenHD] = dfInput.loc[countLenHD]
elif dfInput.loc[countLenHD-1,'Số HĐ'] != dfInput.loc[countLenHD,'Số HĐ'] and intSoHD%3==0:
    dfOutput.loc[countLenHD] = dfInput.loc[countLenHD]
dfOutput.to_excel(writer, sheet_name='Sheet'+str(countSheet), index=False)
writer.save()
writer.close()
print(dfOutput)