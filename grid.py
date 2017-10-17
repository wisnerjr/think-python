def row_complete():
    print('+', end=' ')
    print('- '*4, end='')
    print('+', end=' ')
    print('- '*4, end='')
    print('+')

def columns():
    print('|', end=' ')
    print('  '*4, end='')
    print('|', end =' ')
    print('  '*4, end='')
    print('|')

def row_minor():
    print('+',end=' ')
    print('- '*2, end='')
    print('+')

def column_minor():
    print('|', end=' ')
    print('  '*2, end='')
    print('|')

def grid_11x11():
    row_complete()
    for x in range(0, 4):
        columns()
    row_complete()
    for x in range(0, 4):
        columns()
    row_complete()

def grid_4x4():
    row_minor()
    column_minor()
    column_minor()
    row_minor()
    

grid_11x11()
print()
grid_4x4()
