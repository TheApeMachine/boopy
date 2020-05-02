import logging

class BooEval:

    def __init__(self, ast):
        self.ast    = ast
        self.output = ""

    def Run(self):
        for node in self.ast:
            print(f"booeval.Run({node})")
            self.add(node)

    def add(self, node):
        print(f"booeval.add({self.ast[node]})")
        self.output = sum(map(int, self.ast[node]))
