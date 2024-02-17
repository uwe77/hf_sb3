import json, sys, re
import pandas as pd


def sort_by_world(data, world):
    result = [i for i in data if world in i['title']]
    return result

def sort_by_author(data):
    authors = list(set([i['author'] for i in data]))
    result = {i: [] for i in authors}
    for i in data:
        result[i['author']].append(i)
    return result

if __name__ == "__main__":
    for i in range(1, 13):
        filename = f'hf_rl_fullsearch_p{i}.json'
        with open(filename, 'r') as f:
            data = json.load(f)