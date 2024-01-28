import requests
from bs4 import BeautifulSoup

def search_huggingface(keyword):
    # 构造搜索URL，这里的URL需要根据实际情况修改
    url = f'https://huggingface.co/models/{keyword}'

    # 发送请求
    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to retrieve data')
        return []

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所需数据，这里的选择器需要根据实际页面结构修改
    repos = soup.find_all('div', class_='repo-class')  # 假定类名为'repo-class'

    # 提取和打印信息
    results = []
    for repo in repos:
        repo_name = repo.find('a').text.strip()  # 假定儲存庫名稱在<a>標籤內
        results.append(repo_name)

    return results

# 使用示例
keyword = 'Reinforcement Learning'
repos = search_huggingface(keyword)
for repo in repos:
    print(repo)
