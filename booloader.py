import logging
from boolexer import BooLexer

class BooLoader:

    def __init__(self, filename):
        prog = Program(open(filename, "r"))
        prog.Run()

class Program:

    def __init__(self, fh):
        self.code  = fh
        self.lexer = BooLexer()

    def Run(self):
        for line in self.code:
            print(f"line: {line}")
            self.lexer.Run(line)
            print(f"tokens: {self.lexer.tokens}")

