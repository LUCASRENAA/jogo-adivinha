print("jogo da advinhação")

#crie um input do usuário e gere um numero aleatorio
import random
numero_aleatorio = random.randint(1, 10)
numero_usuario = int(input("Digite um número entre 1 e 10: "))
# sem tentativas
if numero_usuario == numero_aleatorio:
    print("Parabéns! Você acertou o número.")
else:
    print(f"Que pena! O número correto era {numero_aleatorio}. Tente novamente!")

