# Pytaj użytkownika o liczbę tak długo aż poda liczbę parzystą lub przekroczy limit 10 prób

index = 0
while index < 10 :
    shot = int(input("Podaj liczbę: "))
    if shot % 2 == 0:
        print("Udało Ci się....")
        index += 10
    index += 1
if shot % 2 != 0:
    print("Przekroczona liba prób....Niestety")

# Wczytaj numer telefonu użytkownika i rodziel go myślnikami (format XXX-XXX-XXX)
number = input("Podaj numer telefonu: ")
number = number.replace("-", "")
number_clear = ""
print(number_clear)

index = 0
while index < len(number):
    if index % 3 == 0 :
        number_clear += "-"

    number_clear += number[index]
    print(number_clear)
    index += 1
print(number_clear)