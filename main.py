from solutions import sol1
import os

def get_input(day):
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/inputs/{day}'
    return open(input_path, 'r').read()

print(sol1.result(get_input(1)))