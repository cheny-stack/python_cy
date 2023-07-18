import os

# 指定文件夹路径
folder_path = 'C:/Users/47895/Desktop/book/1/鸟儿山'

# 自定义的排序函数，提取文件名中的数字部分进行比较
def sort_by_number(filename):
    # 提取文件名中的数字部分
    digits = ''.join(filter(str.isdigit, filename))
    return int(digits) if digits.isdigit() else filename
# 列出文件夹中的所有文件
file_list = os.listdir(folder_path)

# 根据文件名排序
sorted_file_list = sorted(file_list, key=sort_by_number)

# 打印排序后的文件名
for filename in sorted_file_list:
    print(filename)