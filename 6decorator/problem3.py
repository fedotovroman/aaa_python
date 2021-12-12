import io, sys

def redirect_output(filepath):
    def decorator(func):
        def wrapper(*args, **kwargs):
            old_stdout = sys.stdout
            buffer = io.StringIO()
            sys.stdout = buffer
            func(*args, **kwargs)
            with open(filepath, 'w') as output:
                output.write(sys.stdout.getvalue())
            sys.stdout = old_stdout
        return wrapper
    return decorator

@redirect_output("some_test_data.txt")
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
            print()

calculate()
