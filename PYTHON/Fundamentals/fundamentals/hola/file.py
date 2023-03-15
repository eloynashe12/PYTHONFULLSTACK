num1 = 42 #Esta es una variable de numero entero
num2 = 2.3 #Esta es una variable de numero decimal
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Esto es un arreglo
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#Esto es un arreglo
fruit = ('blueberry', 'strawberry', 'banana')#Esta es un arreglo
print(type(fruit))#verificacion de tipo
print(pizza_toppings[1]) # numeros
pizza_toppings.append('Mushrooms')#cadenas
print(person['name'])#cadenas
person['name'] = 'George'#cadenas
person['eye_color'] = 'blue'#caddenas
print(fruit[2])#numeros

if num1 > 45:#condicional
    print("It's greater")
else:#condicional
    print("It's lower")

if len(string) < 5:#condicional
    print("It's a short word!")
elif len(string) > 15:#condicional
    print("It's a long word!")
else:# condicional
    print("Just right!")

for x in range(5): #bucle
    print(x)
for x in range(2,5):#bucle
    print(x)
for x in range(2,10,3):#bucle
    print(x)
x = 0
while(x < 5):#bucle incrementar
    print(x)
    x += 1

pizza_toppings.pop()#numeros
pizza_toppings.pop(1)#numeros

print(person)#cadenas
person.pop('eye_color')#cadenas
print(person)#cadenas

for topping in pizza_toppings:#bucle
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():#funciones
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x )#funciones
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):#funciones
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#bucles
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)