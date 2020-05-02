import logging
from enum import Enum

class LexState(Enum):
    INIT      = 1
    DELIMITER = 2
    NUMERIC   = 3
    OPERATOR  = 4

class BooLexer:

    def __init__(self):
        self.state  = LexState.INIT
        self.buffer = []
        self.tokens = []

    def Run(self, line):
        for char in line:
            print(f"char: {char}")
            self.getState(char)
            self.handleState()

    def getState(self, char):
        print(f"lexer.getState({self.state})")

        self.state, self.buffer = BooState(self.state, self.buffer, char).NextState()

    def handleState(self):
        print(f"lexer.buffer{self.buffer}")
        print(f"lexer.handleState({self.state})")

        self.tokens.append(BooState(self.state, "".join(self.buffer), None).StateToken())

        # Reset state and buffer for the next round.
        self.state  = LexState.INIT
        self.buffer = []

class BooState:

    def __init__(self, state, buf, char):
        self.state      = state
        self.buffer     = buf
        self.char       = char
        self.delimiters = [":", " "]
        self.operators  = ["+", "-"]

    def NextState(self):
        self.buffer.append(self.char)

        if self.char in self.delimiters:
            return LexState.DELIMITER, self.buffer
        elif self.char in self.operators:
            return LexState.OPERATOR, self.buffer
        elif self.char.isnumeric():
            return LexState.NUMERIC, self.buffer

        # Return the current state by default.
        return self.state, self.buffer

    def StateToken(self):
        return {'id': self.state, 'value': self.buffer}
