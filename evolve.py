from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

def main():
    filename = 'hello.evol'
    file     = open(filename, "r")
    lexer    = Lexer(file)
    parser   = Parser(lexer.tokens)

    lexer.tokenizer()
    print "TOKENS:"
    print lexer.tokens, "\n"

    parser.build_AST()
    print "AST:"
    print parser.AST, "\n"

    evaluator = Evaluator(parser.AST)

    print "OUTPUT:"
    evaluator.run(parser.AST)

if __name__ == "__main__":
    main()
