from utils import *
import requests
GalaxyFileName = 'C:\\Users\\bby\\Desktop\\GalaxyWorkflows.json'
workflows = readJSON(GalaxyFileName)

# 创建一个空列表，用于存储所有工作流的ID
workflow_ids = []

# 遍历工作流列表，并将每个工作流的ID添加到workflow_ids列表中
for workflow in workflows:
    workflow_id = workflow["id"]
    workflow_ids.append(workflow_id)

print(len(workflow_ids))

# 遍历workflow_ids列表，并下载每个工作流的数据
# 拼接id获取各个工具流的详细数据，保存为json文件

# 填写你的API密钥
api_key = "8d874fb05a3f8615b580200b5e530edd"

# 设置请求头，包括API密钥和Galaxy API URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
    "Content-Type": "application/json"
}


for workflow_id in workflow_ids:
    # 设置API URL，其中workflow_id是动态的，将根据循环中的当前ID进行更新

    url = f"https://usegalaxy.org/api/workflows/{workflow_id}/download"

    print(url)

    # 发送GET请求，并使用API密钥获取响应

    response = requests.get(url,headers=headers)

    # 将工作流数据保存到新创建的文件夹中，文件名为workflow_id.ga
    with open(f"D:\\wenjiannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\\_school\\dataset\\Galaxy\\GalaxyJSON\\Galaxy{workflow_id}.json", "wb") as f:
        f.write(response.content)
