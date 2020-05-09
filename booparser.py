import logging
from enum import Enum
from boolexer import LexState, HandleState

class ParseState(Enum):
    INIT    = 1
    ASSIGN  = 2
    RANGE   = 3
    OPERATE = 4

class BooParser:

    def __init__(self, tokens):
        self.tokens    = tokens
        self.ast       = []
        self.state     = ParseState.INIT
        self.hstate    = HandleState.READ
        self.variables = {}
        self.memory    = []
        self.operating = False

    def Run(self):
        for token in self.tokens:
            #print(token)
            self.getState(token)
            #print(f"state: {self.state}")
            #print(f"hstate: {self.hstate}")
            self.handleState(token)
            #print(f"vars: {self.variables}")
            #print(f"mems: {self.memory}")
            #print(f"ast: {self.ast}")

    def getState(self, token):
        self.state, self.hstate = BooParserState(
            self.state, self.hstate, token
        ).NextState()

    def handleState(self, token):
        if self.hstate == HandleState.WRITE:
            self.add_node(token)

            self.state  = ParseState.INIT
            self.hstate = HandleState.READ

    def add_node(self, token):
        if self.state == ParseState.ASSIGN:
            self.handle_assign(token)
        elif self.state == ParseState.RANGE:
            self.handle_range(token)
        elif self.state == ParseState.OPERATE:
            self.handle_operate(token)

    def handle_assign(self, token):
        if token['id'] == LexState.VARIABLE:
            if token['value'] not in self.variables:
                self.variables[token['value']] = None
            else:
                if len(self.memory) == 1:
                    return

                if self.variables[token['value']] in self.memory:
                    if self.operating == False:
                        self.operating = True

                        for m in self.memory:
                            self.ast.append(
                                {"out": self.variables[token['value']]}
                            )

                        self.memory = []
                    else:
                        self.state  = ParseState.OPERATE
                        self.hstate = HandleState.WRITE
                else:
                    self.memory.append(self.variables[token['value']])
        elif token['id'] == LexState.NUMERIC:
            for var in self.variables:
                if self.variables[var] == None:
                    self.variables[var] = token['value']

    def handle_range(self, token):
        try:
            for i in range(int(self.variables[token['value']])):
                self.memory.append(i + 1 + int(self.memory[0]))
        except KeyError:
            self.variables[token['value']] = None

    def handle_operate(self, token):
        for i in self.memory:
            self.ast.append({
                "out": {
                    "add": [int(self.memory[0]), int(i) + 1]
                }
            })

class BooParserState:

    def __init__(self, state, hstate, token):
        self.state     = state
        self.hstate    = hstate
        self.token     = token
        self.operators = ["+"]

    def NextState(self):
        if self.state == ParseState.INIT:
            return self.init_state()
        elif self.state == ParseState.RANGE:
            return self.range_state()
        elif self.state == ParseState.OPERATE:
            return self.operate_state()

    def init_state(self):
        if self.token['id'] == LexState.VARIABLE:
            return ParseState.ASSIGN, HandleState.WRITE
        elif self.token['id'] == LexState.NUMERIC:
            return ParseState.ASSIGN, HandleState.WRITE
        elif self.token['id'] == LexState.KEYWORD:
            return ParseState.RANGE, HandleState.READ
        elif self.token['id'] == LexState.OPERATOR:
            if self.token['value'] in self.operators:
                return ParseState.OPERATE, HandleState.WRITE
            else:
                return self.state, self.hstate

        return self.state, self.hstate

    def range_state(self):
        if self.token['id'] == LexState.VARIABLE:
            return ParseState.RANGE, HandleState.WRITE

        return self.state, self.hstate

    def operate_state(self):
        if self.token['id'] == LexState.VARIABLE:
            return ParseState.OPERATE, HandleState.WRITE

        return self.state, self.hstate
