import requests
from .constants import lexer_path, parser_path
import json
import os

def get_tree(grammar, lexgrammar, input_text, start):
    url = 'http://lab.antlr.org/parse/'
    
    json_string = json.dumps({
        'grammar': grammar,
        'lexgrammar': lexgrammar,
        'input': input_text,
        'start': start
    })
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    response = requests.post(url, data=json_string, headers=headers)
    
    return response.json()

def read_file(path):
    file = open(path, 'r', encoding='utf-8')
    data = file.read()
    file.close()
    return data
    
def generate_parse_tree(input_path, start):
    grammar = read_file(parser_path)
    lexgrammar = read_file(lexer_path)
    input_text = read_file(input_path)
    
    data = get_tree(grammar, lexgrammar, input_text, start)
    
    img_svg = data['result']['svgtree']
    
    file = open('outputs/tree.svg', 'w', encoding='utf-8')
    file.write(img_svg)
    file.close()
    
    file_absolute_path = os.path.abspath('outputs/tree.svg')
    os.system(f'start chrome {file_absolute_path}')
    
    
    