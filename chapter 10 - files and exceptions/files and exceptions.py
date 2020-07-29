with open("files/pi_digits.txt") as file:
    content = file.read()
    print(content.rstrip())

if file.closed:
    print("Fechou!")

for line in open("files/pi_digits.txt"):
    print(line)

file = open("files/pi_digits.txt")

for line in file:
    print(line.rstrip())

file.close()
if file.closed:
    print("Fechou!")
