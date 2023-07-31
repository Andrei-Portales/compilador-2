import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream

from gramar_generated.YALPLexer import YALPLexer
from gramar_generated.YALPParser import YALPParser
from util.generate_tree import generate_parse_tree
from compiler_files.custom_visitor import CustomVisitor

def main():
    parser = argparse.ArgumentParser(description="Procesa archivos.")
    parser.add_argument("-input", metavar="INPUT_FILE", help="Archivo a procesar.")
    args = parser.parse_args()
    
    if not args.input:
        print('No se especificó un archivo -input para procesar.')
        exit(0)

    input_text_path = args.input
    input_stream = FileStream(input_text_path)
    lexer = YALPLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = YALPParser(token_stream)
    tree = parser.program()
    
    # check errors
    if parser.getNumberOfSyntaxErrors() > 0:
        return print('\n\nTiene errores de sintaxis.\n\n')

    # generate_parse_tree(input_text_path, 'program')
    
    visitor = CustomVisitor()
    visitor.visit(tree)
    
    for error in visitor.errors:
        print(error)
    

if __name__ == '__main__':
    main()
