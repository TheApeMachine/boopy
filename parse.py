class Parse:

    def __init__(self, tokens):
        self.tokens = tokens
        self.AST    = []

    def add_node(self, parent, node):
        for a in self.AST:
            if parent in a:
                a[parent].append(node)

    def build_AST(self):
        saved   = {}
        parent  = {}
        collect = False

        for token in self.tokens:
            if token['id'] == 'label':
                t = {token['value']: []}

                if parent != t:
                    parent = token['value']
                    self.AST.append(t)

            elif token['id'] == 'keyword':
                if token['value'] == 'stop':
                    t = {token['value']: 0}
                    self.add_node(parent, t)
                else:
                    if collect == False:
                        saved   = token
                        collect = True
                    else:
                        t = {saved['value']: token['value']}
                        self.add_node(parent, t)
                        collect = False

            elif token['id'] == 'char' or token['id'] == 'atom':
                    if collect == False:
                        saved   = token
                        collect = True
                    else:
                        t = {saved['value']: token['value']}
                        self.add_node(parent, t)
                        collect = False

            elif token['id'] == 'integer':
                if collect == False:
                    if saved == None:
                        self.add_node(parent, token['value'])
                    else:
                        saved   = token
                        collect = True
                else:
                    t = {saved['value']: token['value']}
                    self.add_node(parent, t)
                    collect = False

            elif token['id'] == 'operator':
                if collect == False:
                    saved   = token
                    collect = True
                else:
                    t = {token['value']: [saved['value']]}
                    self.add_node(parent, t)
                    parent = t
                    collect = False
                    saved = None
