from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data

base = Data()

while True:
    text = input("ShadowScript: ")

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree, base)
    result = interpreter.interpret()
    if result is not None:
        print(result)
