from contextlib import contextmanager


@contextmanager
def context_manager(some_argument):
    print('Hey, I started a context, now you are going inside the block of code after "with" keyword')
    yield some_argument + 42
    print('Hey, context is being closed now')


with context_manager(42) as cm:
    print('Block of code after "with" keyword')
    print(cm)

# Output:
# Hey, I started a context, now you are going inside the block of code after "with" keyword
# Block of code after "with" keyword
# 84
# Hey, context is being closed now
