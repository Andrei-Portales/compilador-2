from antlr4 import FileStream, CommonTokenStream

from gramar_generated.YALPLexer import YALPLexer
from gramar_generated.YALPParser import YALPParser


input_stream = FileStream('test/recur.cl')

lexer = YALPLexer(input_stream)


token_stream = CommonTokenStream(lexer)

print('tokens:\n')
# print found tokens
token_stream.fill()
for token in token_stream.tokens:
    print(YALPLexer.symbolicNames[token.type], token.text)
    

print('\n\n')
print('tree:\n')

parser = YALPParser(token_stream)

tree = parser.program()

# print()
# print(tree.toStringTree(recog=parser))

