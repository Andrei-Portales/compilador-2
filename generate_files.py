# Este archivo se encarga de generar los archivos necesarios para el funcionamiento del compilador
# en especifico se encarga de generar los archivos de lexer y parser a partir de los archivos .g4

import subprocess
from util.constants import *

output_path = 'gramar_generated'

subprocess.run(["java", "-jar", antlr_path, "-Dlanguage=Python3", '-o', output_path, lexer_path, parser_path])