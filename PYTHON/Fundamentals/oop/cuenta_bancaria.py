class CuentaBancaria:
    cuentas = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: Cobrando 5$")
            self.balance -= 5
        return self
    
    def display_cuentas_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_cuentas(cls):
        for cuentas in cls.cuentas:
            cuentas.display_cuentas_info()


ahorro = CuentaBancaria(.05,1000)
control = CuentaBancaria(.02,5000)

ahorro.deposito(10).deposito(20).deposito(40).withdraw(600).yeild_interest().display_cuentas_info()
control.deposito(100).deposito(200).deposito(400).withdraw(60).yeild_interest().display_cuentas_info()

CuentaBancaria.print_all_cuentas()
