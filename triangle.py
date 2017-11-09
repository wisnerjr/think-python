def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return "No"
    else:
        return "Yes"


a = int(input("Insert the value of a: "))
b = int(input("Insert the value of b: "))
c = int(input("Insert the value of c: "))

print(is_triangle(a, b, c))