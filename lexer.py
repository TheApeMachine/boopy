class Lexer:

    def __init__(self, data):
        self.data     = data
        self.tokens   = []
        self.keywords = [
            'echo',
            'goto',
            'stop'
        ]

    def tokenizer(self):
        for loc in self.data:
            tmp  = []
            tid  = ''

            for l in loc:
                if l == '"' and tid == '':
                    tid = 'char'
                    tmp = []
                elif l == '"' and tid == 'char':
                    self.tokens.append({'id': tid, 'value': ''.join(tmp)})
                    tid = ''
                    tmp = []
                elif l == ':':
                    self.tokens.append({'id': 'label', 'value': ''.join(tmp)})
                    tmp = []
                elif ''.join(tmp) in self.keywords:
                    self.tokens.append({'id': 'keyword', 'value': ''.join(tmp)})
                    tmp = []
                elif l == "\n":
                    if len(tmp) > 0:
                        self.tokens.append({'id': 'atom', 'value': ''.join(tmp)})
                        tmp = []
                elif l == ' ' and tid != 'char':
                    continue
                else:
                    tmp.append(l)
