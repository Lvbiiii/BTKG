
'''
按照biotools平台提供的JSON文件结构进行信息提取
'''

'''
提取可直接通过键获取的信息，包括：
name,description,homepage,biotoolsId等
'''
from urllib.request import urlopen;
import json
max_page=0
url='https://bio.tools/api/t/?format=json&'

def getSimpleInfo(data,key):
    return data[key]

def getToolInput(data):
    functions=getSimpleInfo(data,'function')
    inputs=[]
    for f in functions:
        input=f['input']
        for i in input:
            inputs.append(i)
    return inputs

def getToolOutput(data):
    functions=getSimpleInfo(data,'function')
    outputs=[]
    for f in functions:
        output=f['output']
        for i in output:
            outputs.append(i)
    return outputs

def getMaxPage():
    rawtext=urlopen(url,timeout=150).read()
    jsonStr = json.loads(rawtext.decode('utf8'))
    return int(jsonStr['count'])//10+1  # 每页有10个数据，//向下取整

def getAndSaveJSON(url,page,output_path):
    rawtext=urlopen(url,timeout=150).read()
    jsonStr = json.loads(rawtext.decode('utf8'))
    f=open(output_path+"BioToolsJSON"+str(page)+".json","a",encoding="utf8");
    f.write(json.dumps(jsonStr, ensure_ascii=False) + "\n"); # 保存前，需要将jsonStr序列化为python相对的数据类型，去掉最后的换行符
    f.close();


def downloadBiotoolsJson(output_path):
    max_page=getMaxPage()
    start_page=1
    # max_page=2841 # 该url下next=null
    for p in range(start_page,max_page+1):   # range(start,stop) 不包括stop
        page_str='page='+str(p)
        getAndSaveJSON(url+page_str,p,output_path)


