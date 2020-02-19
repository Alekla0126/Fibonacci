#Clase Fibonacci
class Fibonacci:
    #Constructor con el numero
    def __init__(self,n):
        self.n = n
    #Funcion iterativa
    def fib(self):
        #Se inician los valores a y b
        a = 0
        b = 1
        #Deste 0 hasta n
        while a < self.n:
            print(a, end=' ')
            a, b = b, a+b
        print()

def main():
    #Se instancia la clase Fibonacci
    f = Fibonacci(400)
    #Se accede al metodo
    f.fib()
main()
