'''
import  openpyxl
path = r'D:\\wenjiannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\\_school\\dataset\\biotolsID2doiDict.xlsx'
table = openpyxl.load_workbook(path)['Sheet']
doi = table.cell(row=1,column=2).value
print(doi)
print(type(doi))
doi1=str(doi).split('/',1)[0]
doi2=str(doi).split('/',1)[1]
print(doi1)
print(doi2)
'''

from bs4 import BeautifulSoup
#准备代码信息，用来练习获取内容
html ="""
<html>
<head><title>The Dormouse's story</title></head>  
<body>  
<h1><b>123456</b></h1>
<p class="title" name="dromouse">
    <b>The Dormouse's story</b>
    aaaaa
</p> 
<p class="title" name="dromouse" title='new'><b>The Dormouse's story</b>a</p>   
<p class="story">Once upon a time there were three little sisters; and their names were  
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,  
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    <a href="http://example.com/tillie" class="siterr" id="link4">Tillie</a>;  
    <a href="http://example.com/tillie" class="siterr" id="link5">Tillie</a>;  
    and they lived at the bottom of a well.
</p>  
<p class="story">...</p>
<ul id="ulone">
    <li>01</li>
    <li>02</li>
    <li>03</li>
    <li>04</li>
    <li>05</li>
</ul>
<div class='div11'>
    <ul id="ultwo">
        <li>0001</li>
        <li>0002</li>
        <li>0003</li>
        <li>0004</li>
        <li>0005</li>
    </ul>
</div>
<div class='div11'>
    <ul id="ultwo">
        <li>0001</li>
        <li>0002</li>
        <li>0003</li>
        <li>0004</li>
        <li>0005</li>
    </ul>
</div>
<ul id="ulone">
    <li>01</li>
    <li>02</li>
    <li>03</li>
    <li>04</li>
    <li>05</li>
</ul>
</body> 
</html>
"""
soup = BeautifulSoup(html,'html.parser')  #选择解析器
data = soup.find_all('div',attrs={'class':'div11'})
print(len(data))
#print(type(data))
if data :
    print(data)
else :
    print("不存在")
#print(type(data.text))

'''
from utils import *
save_file=r'D:\\wenjiannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\\_school\\dataset\\abstract.xlsx'
data = "1"
writeExcel(save_file, 1, 1, data)
'''
