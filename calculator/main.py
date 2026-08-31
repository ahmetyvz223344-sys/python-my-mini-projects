import art
print(art.logo)



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
#böyle iki tane while kullanrakta yapabilirsin

a=True
while a:
    first_number = float(input("Enter the first number: "))
    k = True
    while k:
        for symbols in operation:
            print(symbols)
        operator = input("Enter the operator:")
        second_number = float(input("Enter the second number: "))

        result = operation[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number}={result}")

        again = input(f"type 'y' to continue with {result} or type 'n' to start a new calculation:  ")

        if again == "y":
            first_number = result

        if again == "n":
            k = False





# bu da fonksiyonla başa dönme yolu

def calculater():
    first_number = float(input("Enter the first number: "))
    k = True
    while k:
        for symbols in operation:
            print(symbols)
        operator = input("Enter the operator:")
        second_number = float(input("Enter the second number: "))

        result = operation[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number}={result}")

        again = input(f"type 'y' to continue with {result} or type 'n' to start a new calculation:  ")

        if again == "y":
            first_number = result

        if again == "n":
            k = False
            print("\n"*20)


