from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
import argparse


class Executor:
    def __init__(self):
        self.data = Data()

    def execute(self, path):
        if not path.endswith('.shs'):
            print('Error: Invalid file extension. Supported Extensions:\n -.shs')
            return

        try:
            with open(path) as file:
                lines = file.readlines()
                for idx, line in enumerate(lines):
                    text = line.strip()
                    if text == '':
                        continue
                    elif text.strip() == 'exit':
                        break

                    tokenizer = Lexer(text)
                    tokens = tokenizer.tokenize()

                    parser = Parser(tokens, self.data)
                    tree = parser.parse()

                    interpreter = Interpreter(tree, self.data)
                    result = interpreter.interpret()

                    if result is not None:
                        print(f'{path}:{idx + 1}:', result)

        except:
            print(f'Error: File {path} not found.')


if __name__ == "__main__":
    description = "executor program for ShadowScript"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("path", help="file path")
    args = parser.parse_args()

    executor = Executor()
    executor.execute(args.path)
