import sys
from datetime import datetime

original_write = sys.stdout.write
x = []

def my_write(some_text):
    current_datetime = str(datetime.now().replace(microsecond=0))
    if some_text != '\n':
        original_write(f'[{current_datetime}]: {some_text} \n')

sys.stdout.write = my_write


print('Wake up, Neo...')
print('The Matrix has you...')
print('Follow the white rabbit.')

sys.stdout.write = original_write

print('Knock, knock, Neo.')
