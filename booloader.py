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
        self.code   = fh
        self.tokens = []

    def Run(self):
        for line in self.code:
            #print(f"line: {line}")

            lexer = BooLexer()
            lexer.Run(line)

            for token in lexer.tokens:
                self.tokens.append(token)

        #print(f"tokens: {self.tokens}")

        parser = BooParser(self.tokens)
        parser.Run()
        #print(f"vars: {parser.variables}")
        #print(f"ast:  {parser.ast}")

        evaluator = BooEval(parser.ast)
        evaluator.Run()
        print(f"ouput: {evaluator.output}")
