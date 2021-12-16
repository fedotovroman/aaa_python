import sys
from datetime import datetime

def timed_output(function):
  def wrapper(some_text):
    current_datetime = str(datetime.now().replace(microsecond=0))
    sys.stdout.write(f'[{current_datetime}]: ')
    ret = function(some_text)
    return ret
  return wrapper

#@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')

print_greeting('Nikita')
print_greeting('Roma')
