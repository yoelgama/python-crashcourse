import getpass
import json

# with open("files/pi_digits.txt") as file:
#     content = file.read()
#     print(content.rstrip())
#
# if file.closed:
#     print("Fechou!")
#
# for line in open("files/pi_digits.txt"):
#     print(line)
#
# file = open("files/pi_digits.txt")
#
# for line in file:
#     print(line.rstrip())
#
# file.close()
# if file.closed:
#     print("Fechou!")
#
# lines = open("files/pi_digits.txt").readlines()
# print(lines)
#
# for line in lines:
#     print(line.rstrip())
#
# birth = input("Seu aniversário aparece nos primeiros um milhão de digitos PI? Insira-o aqui: ")
#
# if birth in open("files/pi_million_digits.txt").read().rstrip():
#     print("Yep, seu aniversário está em PI!")
# else:
#     print("No, sorry")

# try:
#     dividendo = int(input("dividendo: "))
#     print("/")
#     divisor = int(input("divisor: "))
#     resposta = dividendo / divisor
# except ValueError:
#     print("Vai dividir letra, arrombado?")
#
# except ZeroDivisionError:
#     print("You funking donkey")
# else:
#     print(resposta)


# json.dump((input("Usuário: "), getpass.getpass("Senha: ")), open("files/donadagrub.json", "w"))
#
# usuario, senha = json.load(open("files/donadagrub.json"))
#
# print(usuario, " ", senha)