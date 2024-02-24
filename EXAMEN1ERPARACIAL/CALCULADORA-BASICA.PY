def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
       return "Error!"
   else:
       return x / y

print("ESCOJA EL TIPO DE OPERACION QUE DESEA HACER:")
print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")
print("4.DiviSION")

choice = input("COLOQUE EL NUMERO Y PRESIONE ENTER")

num1 = float(input("Enter AL PRIMER NUMERO: "))
num2 = float(input("Enter AL SEGUNDO NUMERO: "))

if choice == '1':
   print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
   print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
   print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
   print(num1, "/", num2, "=", divide(num1, num2))

else:
   print("Invalid input")
