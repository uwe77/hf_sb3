import requests, re
from bs4 import BeautifulSoup
import json


def crawl_page(url="https://huggingface.co/models?pipeline_tag=reinforcement-learning&sort=trending", base_url="https://huggingface.co", pattern = "/"+r'[^\/]+'+"/"+r'[^\/]+'):
    data = []
    # Assuming 'html_content' contains the HTML from the file you provided
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all links. You may need to adjust the selector based on the actual HTML structure
    links = soup.find_all('a', href=True)
    i = 0
    for link in links:
        if not re.match(pattern, link['href']):
            continue
        sub_site_url = base_url + link['href']
        i += 1
        print(f"{i} th sub_site: ",sub_site_url)
        response = requests.get(sub_site_url)
        if response.status_code != 200:
            print(f"Failed to access {sub_site_url}")
            continue
        else:
            data.append(crawl_model_page(sub_site_url))
    return data

def crawl_model_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取<meta property="og:title">的content属性值
        title_tag = soup.find("meta", property="og:title")
        title = title_tag["content"] if title_tag else "Title Not Found"
        
        # 提取<body>标签下的所有内容
        body_content = soup.body
        if body_content is not None:
            body_content = body_content.get_text()
        else:
            body_content = "Body Not Found"
        
        # 将<body>内容转换为字符串
        body_html = str(body_content)
        
        return {
            "title": title,
            "url": url,
            "body_html": body_html
        }
    else:
        return
    
def save_to_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    site = "https://huggingface.co/models?pipeline_tag=reinforcement-learning&sort=trending"
    print(site[:-13])
    pages= 1249
    data = []
    for i in range(pages):
        print(f"**************Processing page {i+1}/{pages}**************")
        url = site
        if i != 0:
            url = site[:-13]+f'p={i}'+site[-14:]
        page_data = crawl_page(url=url, pattern = "/"+r'[^\/]+'+"/"+r'[^\/]+')
        data.extend(page_data)
    save_to_json(data)