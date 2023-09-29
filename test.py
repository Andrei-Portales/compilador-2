import jinja2

TEMPLATE_PATH = 'compiler_files/templates/intern_code_template.j2'

template = jinja2.Template(open(TEMPLATE_PATH).read())

data = {
    'functions': [
        {
            'name': '_foo',
            'is_main': False,
            'bytes': 10,
            'body': [],
        },
        {
            'name': 'main',
            'is_main': True,
            'bytes': 80,
            'body': [],
        },  
          
    ],
}

output = template.render(data)

with open('compiler_files/outputs/intern_code.ac', 'w', encoding='utf-8') as f:
    f.write(output)
    
    
    TEMPLATE = 'lexer/templates/template.py.j2'


# def fill_template(variables):
#     template = jinja2.Template(open(TEMPLATE).read())
#     template = template.render(variables)

#     if not os.path.exists(os.path.dirname('lexer/output/lexer.py')):
#         os.makedirs(os.path.dirname('lexer/output/lexer.py'))

#     file = open('lexer/output/lexer.py', 'w')
#     file.write(template)
#     file.close()