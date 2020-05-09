import logging

class BooEval:

    def __init__(self, ast):
        self.ast       = ast
        self.output    = ""

    def Run(self):
        for node in self.ast:
            print(f"node: {node}")

            for key, value in node.items():
                getattr(self, key)(value)

    def out(self, value):
        if isinstance(value, dict):
            for key, value in value.items():
                getattr(self, key)(value)
        else:
            self.output += value + "\n"

    def add(self, values):
        self.output += str(sum(map(int, values))) + "\n"
