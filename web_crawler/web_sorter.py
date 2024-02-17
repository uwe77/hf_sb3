import json, sys, re
import pandas as pd


def sum_of_world(world, key='describe'):
    for i in range(13):
        filename = f'hf_rl_fullsearch_p{i+1}.json'
        result = 0
        with open(filename, 'r') as f:
            data = json.load(f)
            sys.stdout.write("\r")
            sys.stdout.write("**************Processing page {:2d}**************".format(i+1))
            sys.stdout.flush()
            for d in data: 
                if world in d[key]:
                    result += 1
    sys.stdout.write("\rComplete!                                      \n")
    return result

def sun_of_author(author, key='author'):
    for i in range(13):
        filename = f'hf_rl_fullsearch_p{i+1}.json'
        result = 0
        with open(filename, 'r') as f:
            data = json.load(f)
            sys.stdout.write("\r")
            sys.stdout.write("**************Processing page {:2d}**************".format(i+1))
            sys.stdout.flush()
            for d in data: 
                if author in d[key]:
                    result += 1
    sys.stdout.write("\rComplete!                                      \n")
    return result

if __name__ == "__main__":
    print(sum_of_world('a2c'))