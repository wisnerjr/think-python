def print_twice(str):
    print(str)

def do_twice(f, str):
    f(str)
    f(str)

def print_four(str):
    print(str)
    print(str)

def do_four(f, str):
    f(str)
    f(str)


do_twice(print_twice, 'test')

print()

do_four(print_four, 'four')