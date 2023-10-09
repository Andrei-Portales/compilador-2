import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream

from gramar_generated.YALPLexer import YALPLexer
from gramar_generated.YALPParser import YALPParser
from util.generate_tree import generate_parse_tree
from compiler_files.custom_visitor import CustomVisitor

from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self, error_callback):
        super().__init__()
        self.error_callback = error_callback

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Line {line}:{column} -> {msg}"
        self.error_callback(error_message)


def main():
    parser = argparse.ArgumentParser(description="Procesa archivos.")
    parser.add_argument("-input", metavar="INPUT_FILE", help="Archivo a procesar.")
    args = parser.parse_args()
    
    if not args.input:
        print('No se especificó un archivo -input para procesar.')
        exit(0)
        
    def error_callback(x):
        print('error_callback', x)

    input_text_path = args.input
    input_stream = FileStream(input_text_path)
    lexer = YALPLexer(input_stream)
    lexer.addErrorListener(CustomErrorListener(error_callback))
    
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = YALPParser(token_stream)
    parser.addErrorListener(CustomErrorListener(error_callback))
    tree = parser.program()
    
    
    # check errors
    if parser.getNumberOfSyntaxErrors() > 0:
        return error_callback(parser.getNumberOfSyntaxErrors())

    visitor = CustomVisitor(error_callback)
    
    # try:
    visitor.visit(tree)
    # except Exception as e:
    #     print(e)
    #     pass
        
    

if __name__ == '__main__':
    main()
