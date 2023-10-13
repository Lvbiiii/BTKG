from bs4 import BeautifulSoup
import urllib.request
import re
import time
import traceback
import pandas as pd
import warnings
from openpyxl import load_workbook
from utils import *
import requests

warnings.filterwarnings("ignore")


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/116.0.0.0 Safari/537.36'}

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

def get_paper_page(url):
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req, timeout=100)
    html = res.read().decode('utf-8')

    # proxy = get_proxy().get("proxy")
    # html = requests.get(url, headers=headers, proxies={"http": "http://{}".format(proxy)})

    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('div', attrs={'class': 'gs_rs gs_fma_s'}) is not None:
        data = soup.find('div', attrs={'class': 'gs_rs gs_fma_s'}).text
    elif len(soup.find_all('div', attrs={'class': 'gs_rs'})) == 1:   # <body>下唯一
        data = soup.find('div', attrs={'class': 'gs_rs'}).text
    else:
        data = "未能正确检索"
    return data

'''
def save_paper_list(data, myrow, mycolumn, file_name):
    data = pd.DataFrame(data, columns=['paper title', 'reference', 'publish info', 'url'])
    writer = pd.ExcelWriter(file_name)
    data.to_excel(writer, index=False, encoding='utf-8', sheet_name='Sheet1')
    writer.save()
    writer.close()
'''


def get_paper_list_by_doi(doi, myrow, mycolumn, max_capacity = 100, debug_mode = False, save_file = "./abstract.xlsx", retry_times = 5):
    url_base = 'https://scholar.google.com/scholar?hl=zh-CN&as_sdt=0%2C5&q='
    # doi1 = str(doi).split('/')[0]
    # doi2 = str(doi).split('/')[1]
    doi1 = doi.replace('/', '%2F')
    url = url_base + doi1 + "&btnG="
    data = ''
    print(url)
    for i in range(retry_times):
        try:
            print(myrow)
            data = get_paper_page(url)
            break
        except Exception as e:
            if i < retry_times -1:
                print("error, retrying ... ")
            else:
                print("error, fail to get ", url)
            if debug_mode:
                traceback.print_exc()
            time.sleep(20)
    time.sleep(10)
    # data: [论文标题, 引用数, 发表时间及机构缩写, 论文链接]
    print(data)
    writeExcel(save_file, myrow, mycolumn,data)

if __name__ == "__main__":
    InPutPath = r'D:\\wenjiannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\\_school\\dataset\\biotolsID2doiDict.xlsx'
    OutputPath = r'D:\\wenjiannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\\_school\\dataset\\abstract.xlsx'
    TableColumn = 2
    for Tablerow in range(1223,2000):
        doi = readExcel(InPutPath, Tablerow, TableColumn)
        get_paper_list_by_doi(doi, Tablerow, TableColumn, max_capacity=100, debug_mode=False, save_file=OutputPath)
    print("end")

