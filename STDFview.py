import pandas as pd

with open('main_Lot_1_Wafer_1_Oct_13_09h33m41s_STDF', 'rb') as file:
    data = file.read()

def Serch_partid(i):
    # 判斷part後面的
    part_value =int(data[i+19])
    
    if part_value == 1:
        num_part = 1
    elif part_value == 2:
        num_part = 2
    
    return num_part


for i in range(len(data)):
       #判斷PPR位置
    if data[i:i+2] == (b'\x05\x14') :
        #print('起始點',i)
        #2024 01/10新增
           # 将 data 转换为 bytearray
                #print("找到566!")
                #mutable_data = bytearray(data)
                #mutable_data[i+9:i+11] = b'\x10\x10'
                #modified_data = bytes(data)
                #Solfbin = modified_data[i+9:i+11]
                #Solfbin = int.from_bytes(Solfbin, byteorder='little', signed=True)
        
        x_byte = data[i+11:i+13]
        x_coordinate = int.from_bytes(x_byte, byteorder='little', signed=True)
        y_byte = data[i+13:i+15]
        y_coordinate = int.from_bytes(y_byte, byteorder='little', signed=True)
        y_coordinate = int.from_bytes(y_byte, byteorder='little', signed=True)
        partnum=Serch_partid(i)
        part_id=data[i+20:i+20+partnum]
        part_id_value = int(part_id)
        print('X座標為:',x_coordinate,'Y座標為:',y_coordinate,'part id:',part_id_value,'bin:',Solfbin)



# 創造新文件
#with open('ectortest.stdf', 'wb') as new_file:
    #new_file.write(modified_data)
        

MAPdata = [
    {"X座標": -5, "Y座標": -4, "PART ID": 1},
    {"X座標": -1, "Y座標": -4, "PART ID": 2},
    {"X座標": 4, "Y座標": -4, "PART ID": 3},
    {"X座標": 6, "Y座標": -4, "PART ID": 4},
    {"X座標": 7, "Y座標": -4, "PART ID": 5},
    {"X座標": -7, "Y座標": -3, "PART ID": 6},
    {"X座標": -3, "Y座標": -3, "PART ID": 7},
    {"X座標": -2, "Y座標": -3, "PART ID": 8},
    {"X座標": 3, "Y座標": -3, "PART ID": 9},
    {"X座標": 4, "Y座標": -3, "PART ID": 10},
    {"X座標": 6, "Y座標": -3, "PART ID": 11},
    {"X座標": -6, "Y座標": 0, "PART ID": 12},
    {"X座標": -4, "Y座標": 0, "PART ID": 13},
]

# 創建一個dataFrame
df = pd.DataFrame(MAPdata)

# 生成X座標和Y座標
x_range = list(range(min(df["X座標"]), max(df["X座標"]) + 1))
y_range = list(range(min(df["Y座標"]), max(df["Y座標"]) + 1))

# 創一個空的來填結果
result_df = pd.DataFrame(index=y_range, columns=x_range)

# 填充结果DataFrame
for _, row in df.iterrows():
    result_df.at[row["Y座標"], row["X座標"]] = row["PART ID"]

result_df.to_excel("wafer_map.xlsx")

print("Excel表格已生成：wafer_map.xlsx")





import openpyxl
from openpyxl.styles import PatternFill

# 读取Excel文件
excel_file_path = "path/to/your/file.xlsx"
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# 定义好和坏的bin
good_bin_values = [1, 3, 9]
bad_bin_values = [5, 6]

# 循环遍历除第一行和第一列之外的所有单元格
for row in range(2, sheet.max_row + 1):
    for col in range(2, sheet.max_column + 1):
        cell_value = sheet.cell(row=row, column=col).value

        # 根据条件设置背景颜色
        if cell_value in good_bin_values:
            sheet.cell(row=row, column=col).fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")  # 绿色
        elif cell_value in bad_bin_values:
            sheet.cell(row=row, column=col).fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")  # 红色

# 保存修改后的Excel文件
wb.save("path/to/your/modified_file.xlsx")
