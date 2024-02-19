import json, sys, re, gdown, os
import pandas as pd
from collections import defaultdict


def download_data():
    url = "http://gofile.me/773h8/d6Vj2olW6"
    gdown.download(url, output="hf_rl_fullsearch.ZIP" ,quiet=False)
    os.system('unzip hf_rl_fullsearch')

def sum_of_word(word, key='describe'):
    for i in range(13):
        filename = f'hf_rl_fullsearch_p{i+1}.json'
        result = 0
        with open(filename, 'r') as f:
            data = json.load(f)
            sys.stdout.write("\r")
            sys.stdout.write("**************Processing page {:2d}**************".format(i+1))
            sys.stdout.flush()
            for d in data: 
                if word in d[key]:
                    result += 1
    sys.stdout.write("\rComplete!                                      \n")
    return result

def sort_by_author():
    results = defaultdict(str)
    for i in range(13):
        filename = f'hf_rl_fullsearch_p{i+1}.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            sys.stdout.write("\r")
            sys.stdout.write("**************Processing page {:2d}**************".format(i+1))
            sys.stdout.flush()
            for d in data:
                results[d['author']] += f"{d['model_name']}\n"
    sys.stdout.write("\rComplete!                                      \n")
    with open('rl_models_sorted_by_author.json', 'w') as f:
        json.dump(results, f, indent=4)

def authors_models_num():
    results = defaultdict(int)
    for i in range(13):
        filename = f'hf_rl_fullsearch_p{i+1}.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            sys.stdout.write("\r")
            sys.stdout.write("**************Processing page {:2d}**************".format(i+1))
            sys.stdout.flush()
            for d in data:
                results[d['author']] += 1
    sys.stdout.write("\rComplete!                                      \n")
    sorted_result = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    with open('rl_models_num_sorted_by_author.json', 'w') as f:
        json.dump(sorted_result, f, indent=4)

if __name__ == "__main__":
    # authors_models_num()
    while True:
        # key = input("Please input the class you want to search: ")
        # if key == 'q':
        #     break
        word = input("Please input the key word you want to search: ")
        if word == 'q':
            break
        print(sum_of_word(word, 'model_name'))
