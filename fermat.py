def check_fermat(a, b, c, n):
    if(n == 2):
        return "That Pythagoras dude done already!"
    else:
        catetos = (int)(a**n) + (int)(b**n)
        hipotenusa = (int)(c**n)
        if (catetos == hipotenusa):
            return "Holy smokes, Fermat was wrong!"
        else:
            return "No, that doesn’t work."





a = int(input('What value to use for a?\n'))
b = int(input('What value to use for b?\n'))
c = int(input('What value to use for c?\n'))
n = int(input('What value to use for n?\n'))

print(check_fermat(a, b, c, n))