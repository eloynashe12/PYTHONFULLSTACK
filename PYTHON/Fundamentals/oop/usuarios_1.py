class Usuario:

    def __init__(self, name, email_address,) -> None:
        self.name = name
        self.email = email_address
        self.balance_cuenta= 0

    def hacer_depósito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount


    def imprime(self):
        print(f"{self.name} monto {self.balance_cuenta}")
      
    

xuly = Usuario("Eloy", "miCorreo")
mateo= Usuario("Mateo" ,"Correo@correo.cl")
diego= Usuario("Diego","correo@corre.com")

xuly.hacer_depósito(1000000)
xuly.hacer_depósito(5000000)
xuly.hacer_depósito(1000)
xuly.hacer_retiro(3000000)
xuly.hacer_retiro(2000000)

mateo.hacer_depósito(5000000)
mateo.hacer_depósito(2000000)
mateo.hacer_retiro(1000000)
mateo.hacer_retiro(50000)

diego.hacer_depósito(1000000)
diego.hacer_retiro(5000)
diego.hacer_retiro(500000)
diego.hacer_retiro(25000)
diego.hacer_depósito(2000000)
print("El usuario:", xuly.name, "tiene en su cuenta;", xuly.balance_cuenta)

print("El usuario;", mateo.name,"tiene en su cuenta;", mateo.balance_cuenta )

print("El usuario", diego.name,"tiene en su cuenta;", diego.balance_cuenta)
