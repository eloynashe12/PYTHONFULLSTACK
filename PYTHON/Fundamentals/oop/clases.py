
# class Usuario:		
#     def __init__(self) -> None:
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.balance_cuenta = 0
#         self.apellido = "boy"
#         self.sexo = "pansexual"
#         self.bank_name = "dojo credit union"

# Usuario()
# guido = Usuario()
# monty = Usuario()
# teo   = Usuario()
# print(guido.name)	
# print(monty.name)
# print(teo.email)

# guido.name = "xhuly"
# print(guido.name, guido.apellido ,"y soy" , guido.sexo) 

# guido = Usuario()
# monty = Usuario()
# guido.nombre_banco = "Dojo Credit Union"
# print(guido.bank_name)  
# print(monty.bank_name)



class Usuario:

    def __init__(self , name, email_address,balance,sexo):
        self.name = name
        self.email = email_address
        self.balance_cuenta = balance
        self.sexo=sexo
        
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
    	self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la 

guido = Usuario("Guido van Rossum", "guido@python.com",0,"machoteee")
xhuly = Usuario("chulito","correo@dfgdf",1000,"loktron")



print(xhuly.name, xhuly.email,"tengo en mi cuenta" ,xhuly.balance_cuenta, "y soy un:" ,xhuly.sexo)


xhuly.hacer_depósito(666)

print(xhuly.balance_cuenta)
