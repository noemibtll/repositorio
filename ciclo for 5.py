a = 0
b = 1
n = int ( input ("inrese numero entero"))
for i in range(1, n):
    c = a + b
    a = b
    b = c
    print (b, " ", end="")
