#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#R:La Respuesta de esta funcion es = 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#R:En esta funcion hay un error Porque number_of_days_in_a_week_silicon_or_triangle_sides es una funcion que no esta declarada

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#R:La Respuesta de esta funcion es 5, porque siempre se toma el primer return el segundo queda nulo

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#R La respueta es 5,Porque ya retorno y no va  imprimir un numero no declarado

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#R: la respuesta es 5 

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#R:El Error de esata funcion es que no se pueden sumar 2 funciones


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#R La respuesta declarada de esta funcion es 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#R la respuesta de esta funciuon es 100 y 10 y no va a retornar en 7 ya que el primer return ya esta declarado como 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#R La respuesta de esta funcion es 7,14 y 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#R:La respuesta es 8,me retorna b+c y no return 10 ya que b+c esta en primer posicion

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#R:Las respuestas son 500,500,300 y 500

#12
b = 500

print(b)#500

def foobar():
    b = 300
    print(b)
    return b

print(b) #500

foobar()#300

print(b) #500

#R:Las respuestas son 500,500,300,500

#13
b = 500
print(b)#500

def foobar():
    b = 300
    print(b)
    return b

print(b)#500

b=foobar()#300

print(b)#300

#R:Las respuesta son 500,500,300 y 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#R:Las respuestas son 1,3,2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#R:Las Respuestas son 1,3,5,10