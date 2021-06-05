from rply import ParserGenerator
from ast import Num, Add, Subtract, Print, Multiply, Divide


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        # @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : expression ADD expression')
        @self.pg.production('expression : expression SUBTRACT expression')
        @self.pg.production('expression : expression MULTIPLY expression')
        @self.pg.production('expression : expression DIVIDE expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'ADD':
                return Add(left, right)
            elif operator.gettokentype() == 'SUBTRACT':
                return Subtract(left, right)
            elif operator.gettokentype() == 'MULTIPLY':
                return Multiply(left, right)
            elif operator.gettokentype() == 'DIVIDE':
                return Divide(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Num(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()