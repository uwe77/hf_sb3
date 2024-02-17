import requests, re, time, sys
from bs4 import BeautifulSoup
import json


def crawl_page(url="https://huggingface.co/models?pipeline_tag=reinforcement-learning&sort=trending", base_url="https://huggingface.co", pattern = "/"+r'[^\/]+'+"/"+r'[^\/]+'):
    data = []
    # Assuming 'html_content' contains the HTML from the file you provided
    response = requests.get(url)
    if response.status_code != 200:
        # print(f"Failed to access {url}")
        sys.stdout.write("\r")
        sys.stdout.write("Failed to access {}".format(url))
        sys.stdout.flush()
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
        # print(f"{i} th sub_site: ",sub_site_url)
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} th sub_site: {}".format(i, sub_site_url))
        sys.stdout.flush()
        response = requests.get(sub_site_url)
        if response.status_code != 200:
            sys.stdout.write("\r")
            sys.stdout.write("Failed to access {}".format(sub_site_url))
            sys.stdout.flush()
            continue
        else:
            tmp = crawl_model_page(sub_site_url)
            if tmp is not None:
                data.append(tmp)
    return data

def crawl_model_page(url, pattern = r'[^\/]+'+"/"+r'[^\/]+'):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 提取<meta property="og:title">的content属性值
        title_tag = soup.find("meta", property="og:title")
        title = title_tag["content"] if title_tag else "Title Not Found"
        if not re.match(pattern, title):
            return
        title = title.replace(" \u00b7 Hugging Face", "")
        author = title.split("/")[0]
        model_name = title.split("/")[1]
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
            "author": author,
            "model_name": model_name,
            "url": url,
            "describe": body_html
        }
    else:
        return
    
def save_to_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    site = "https://huggingface.co/models?pipeline_tag=reinforcement-learning&sort=trending"
    print(site[:-13])
    pages= 1248
    data = []
    file_num = 1
    try:
        for i in range(pages):
            print(f"**************Processing page {i+1}/{pages}**************")
            url = site
            if i != 0:
                url = site[:-13]+f'p={i}'+site[-14:]
            page_data = crawl_page(url=url, pattern = "/"+r'[^\/]+'+"/"+r'[^\/]+')
            data.extend(page_data)
            save_to_json(data, f"hf_rl_fullsearch_p{file_num}.json")
            print("\n**************Saved current data**************")
            if i % 100 == 0 and i != 0:
                print("**************100 pages achieved**************",
                      "\n",
                      "**************Sleeping for 10s***************")
                for remaining in range(120, 0, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\rComplete!            \n")
                print("**************start next 100 pages************")
                file_num += 1
    except:
        print("Error occured")