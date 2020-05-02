import logging
from boolexer import LexState

class BooParser:

    def __init__(self, tokens):
        self.tokens      = tokens
        self.ast         = {}
        self.current_key = None
        self.memory      = []

    def Run(self):
        for token in self.tokens:
            if token['id'] == LexState.NUMERIC:
                self.store_memory(token['value'])

                if len(self.memory) > 0 and self.current_key != None:
                    self.dump_memory()
            elif token['id'] == LexState.OPERATOR:
                self.add_node(token['value'])

    def store_memory(self, value):
        self.memory.append(value)

    def dump_memory(self):
        self.ast[self.current_key] = self.memory
        self.memory = []
        self.current_key = None

    def add_node(self, key):
        self.ast[key] = []
        self.current_key = key
