from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lang_lex = LexerGenerator()

    def _add_tokens(self):
        self.lang_lex.add('OPEN_PAREN', r'\(')
        self.lang_lex.add('CLOSE_PAREN', r'\)')
        self.lang_lex.add('SEMI_COLON', r'\;')
        self.lang_lex.add('PRINT', r'print')
        self.lang_lex.add('ADD', r'\+')
        self.lang_lex.add('SUBTRACT', r'\-')
        self.lang_lex.add('MULTIPLY', r'\*')
        self.lang_lex.add('DIVIDE', r'\/')
        self.lang_lex.add('NUMBER', r'\d+')
        self.lang_lex.ignore('\s+')

    def get_lang_lex(self):
        self._add_tokens()
        return self.lang_lex.build()