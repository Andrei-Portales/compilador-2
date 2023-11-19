import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream

from ThreeAdress_parser.ThreeAddressCodeLexer import ThreeAddressCodeLexer
from ThreeAdress_parser.ThreeAddressCodeParser import ThreeAddressCodeParser
from util.generate_tree import generate_parse_tree
from ThreeAdress_parser.ThreeAddressCodeCustomVisitor import ThreeAddressCodeCustomVisitor

from antlr4.error.ErrorListener import ErrorListener

def main():
    threeadresscodepath = "compiler_files/outputs/intern_code.ac"
    input_stream = FileStream(threeadresscodepath)
    lexer = ThreeAddressCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ThreeAddressCodeParser(token_stream)
    tree = parser.program()
    visitor = ThreeAddressCodeCustomVisitor()
    # visitor.visit(tree)
    # visitor.print_code()
    # print strucutre of tree
    print(Trees.toStringTree(tree, None, parser))
    print("done")

if __name__ == '__main__':
    main()
