def sayhello(to=None):
    if to:
        return f'Hello, {to}!'
    return 'Hello!'

def escape_func(input = None):
    if input:
        return input
    else:
        return "escape_func"