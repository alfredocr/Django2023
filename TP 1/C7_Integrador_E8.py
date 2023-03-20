"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.

"""

class CUENTA():
    def __init__(self, titular, cantidad=0):
        self.__titular = str(titular)
        self.__cantidad = float(cantidad)


    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad = valor


    def mostrar(self):
        print("Titular de la cuenta: " + self.titular.title())
        print("Monto en la cuenta : " + str(self.cantidad)) 

    def ingresar_cantidad(self):
        ing_valor = float(input("Informe el monto a ingresar : "))
        if  ing_valor > 1:
            self.cantidad = ing_valor
        else : 
            print("El valor ingresado debe ser mayor a 1, vuelva a intentarlo")

    def retirar(self):
        ret_valor = float(input("Ingrese el monto a retirar : "))
        self.cantidad = self.cantidad - ret_valor
        return self.cantidad


class CUENTA_JOVEN(CUENTA):
    def __init__(self, titular, cantidad, bonifica=0):
        super().__init__(titular, cantidad=0)
        self.__bonificación = bonifica
    
    @property
    def bonificación(self):
        return self.__bonificación
    
    @bonificación.setter
    def bonificación(self, valor):
        self.__bonificación = valor

    def es_titular_valido(self):
        
        edad_valida = int(input("Ingrese la edad del titular : "))
        if(edad_valida >= 18) and (edad_valida < 25) :
            return True
        else :
            return False
        
            
    def retirar(self):
        if (self.es_titular_valido()):
            super().retirar()
        else :
            print("No puede retirar dinero, usuario no hailitado")


    def mostrar(self):
        print ("Cuenta Joven")
        print ("Bonificación de la cuenta :",self.bonificación, "%")
        
        

 
c2 = CUENTA_JOVEN("Santino", 2)
c2.bonificación = 30
c2.retirar()
c2.mostrar()

