import logging

class BooEval:

    def __init__(self, ast):
        self.ast       = ast
        self.output    = ""
        self.operators = {'+': 'add'}

    def Run(self):
        for node in self.ast:
            print(f"booeval.Run({node})")

            n = node

            if node in self.operators:
                n = self.operators[node]

            getattr(self, n)(self.ast[node])

    def add(self, values):
        print(f"booeval.add({values})")
        self.output = sum(map(int, values))
