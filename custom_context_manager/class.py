# Example of custom context manager

class A:
    def __enter__(self):
        print('Hey, I started a context, now you are going inside the bloke of code after "with" keyword')
        return 42

    def __exit__(self, exc_type, exc_value, traceback):
        print('Hey, context is being closed now')


with A() as a:
    print('Bloke of code after "with" keyword')
    print(f'By the way, here is what I put in context manager variable, it is just a return value of __enter__: {a}')

# Output:
# Hey, I started a context, now you are going inside the bloke of code after "with" keyword
# Bloke of code after "with" keyword
# By the way, here is what I put in context manager variable, it is just a return value of __enter__: 42
# Hey, context is being closed now
