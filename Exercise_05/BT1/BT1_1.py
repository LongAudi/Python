import pandas as pd

df1 = pd.read_excel('./Exercise_05/BT1/Nhanvien.xlsx',sheet_name=0,dtype=object,header=5)
df2 = pd.read_excel('./Exercise_05/BT1/thongtinnhanvien.xlsx',sheet_name=0,dtype=object,header=3)
df3 = df2.copy()
df3['Tên'] = ''
# print(df1)
# print(df2)
# print(df1.query('MSNV == 114066'))
for index,row in df2.iterrows():
    msnv = row['MSNV']
    a = df1.query('MSNV == @msnv')
    print(a.iloc[0]['Tên'])
    df3.at[index,'Tên'] = a.iloc[0]['Tên']
print(df3['Tên'])  
df3.to_excel("D:\BTPython\Exercise_05\BT1\output.xlsx",index=False)  