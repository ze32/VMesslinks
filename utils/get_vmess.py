import os
from datetime import datetime

import requests

# 获取今天的日期
year = datetime.now().year
month = datetime.now().strftime("%m")
day = datetime.now().strftime("%d")

# 构建 URL，日期部分会自动替换为当前日期
url = f"https://clashnode.cc/uploads/{year}/{month}/0-{year}{month}{day}"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

v2ray_node = ''
clash_node = ''

# 发送 HTTP 请求获取链接内容
try:
    v2ray_response = requests.get(url+'.txt', headers=headers)
    clash_response = requests.get(url+'.yaml', headers=headers)
    v2ray_response.raise_for_status()  # 检查请求是否成功
    clash_response.raise_for_status()

    print(f"成功获取到 v2ray_node 内容 (日期: {year}-{month}-{day}):")
    v2ray_node = v2ray_response.text
    print(v2ray_node)
    print('-------------------------------------------------------------------------------------')
    print(f"成功获取到 clash_node 内容 (日期: {year}-{month}-{day}):")
    clash_node = clash_response.text
    # print(clash_node)

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")

# 将去重后的节点信息保存到文件
# with open("./links/v2ray", "w") as f:
#     f.write(v2ray_node)
# with open("./links/clash", "w") as f:
#     f.write(clash_node)

# 定义文件夹路径
links_directory = "./links"

# 创建目录，如果不存在
os.makedirs(links_directory, exist_ok=True)

# 写入 v2ray 文件
with open(os.path.join(links_directory, "v2ray"), "w", encoding='utf-8') as f:
    if v2ray_node:
        f.write(v2ray_node)

# 写入 clash 文件
with open(os.path.join(links_directory, "clash"), "w", encoding='utf-8') as f:
    if clash_node:
        f.write(clash_node)

print("节点信息已保存")
