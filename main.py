from parser import Parser
from lexer import Lexer

text_input = """print(4*2-3*2);"""

lexer = Lexer().get_lang_lex()
tokens = lexer.lex(text_input)

parser_gen = Parser()
parser_gen.parse()
parser = parser_gen.get_parser()
parser.parse(tokens).eval()