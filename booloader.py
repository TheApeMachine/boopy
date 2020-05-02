import logging
from boolexer import BooLexer
from booparser import BooParser
from booeval import BooEval

class BooLoader:

    def __init__(self, filename):
        prog = Program(open(filename, "r"))
        prog.Run()

class Program:

    def __init__(self, fh):
        self.code = fh

    def Run(self):
        for line in self.code:
            print(f"line: {line}")

            lexer = BooLexer()
            lexer.Run(line)
            print(f"tokens: {lexer.tokens}")

            parser = BooParser(lexer.tokens)
            parser.Run()
            print(f"ast: {parser.ast}")

            evaluator = BooEval(parser.ast)
            evaluator.Run()
            print(f"ouput: {evaluator.output}")
