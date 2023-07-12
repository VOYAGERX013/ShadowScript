from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input('ShadowScript: ').strip()

    if text == '':
        continue
    elif text == 'exit':
        break

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens, base)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    if result is not None:
        print(result)
