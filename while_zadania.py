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
    if index % 3 == 0 and index != 0:
        number_clear += "-"

    number_clear += number[index]
#    print(number_clear)
    index += 1
print(number_clear)

#####################################################################

# Poproś użytkownika o podanie ulubionych dań, rozdzielając każde z nich przecinkiem

# Nadstępnie wypisz każde z nich wraz z informacją, które miejsce na jej/jego liście.

food = input("Podaj ulubioną listę dań, rozdzielając je przecinkiem: ")
list = food.split(",")
print(f"Lista jaką podałeś: {list}")
index =0
index_1 = 0
while index < len(list):
    index_1 +=1
    print(f" Na pozycji {index_1} znajduje się {list[index]}")
    index += 1