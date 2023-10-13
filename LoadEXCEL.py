from openpyxl import Workbook

from utils import loadNpy


def write_dict_to_excel(data_dict, filename):
    # 创建一个新的Excel工作簿
    workbook = Workbook()

    # 获取活动的工作表
    worksheet = workbook.active

    # 写入字典的键作为表头
    headers = list(data_dict.keys())
    worksheet.append(headers)

    # 写入字典的值
    values = list(data_dict.values())
    worksheet.append(values)

    # 保存Excel文件
    workbook.save(filename)

# 示例字典
my_dict = loadNpy('D:\\wenjiannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\\_school\\dataset\\output\\biotolsID2doiDict.npy').item()

# 调用函数将字典写入Excel文件
write_dict_to_excel(my_dict, 'biotolsID2doiDict.xlsx')
