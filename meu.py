def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    if y != 0:
        return x / y
    else:
        print("Não é possível dividir por 0.")

print("Selecione a opção:")
print("1. adição")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")

escolha = input("Digite 1/2/3/4: ")

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))

if escolha == '1':
    print(f"{num1} + {num2} = {adicao(num1,num2)}")
elif escolha == '2':
    print(f"{num1} - {num2} = {subtracao(num1, num2)}")
elif escolha == '3':
    print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
elif escolha == '4':
    print(f"{num1} / {num2} = {divisao(num1, num2)}")
else:
    print("Opção inválida.")