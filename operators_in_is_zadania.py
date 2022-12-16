# Sprawdź czy w liście zakupów najjduje się chleb lub bułki

shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shopping_list = shopping_elements.split(",")

if "chleb" in shopping_list or "bułki" in shopping_list :
    print("Planujesz kupić pieczywo")
else:
    print("Nie znalazłem na liscie zakupów ani bułek ani chleba")



# podaj swój numer telefonu i sprawdzić czy jest tam zero

number = input("Podaj swój nume rtelefonu: ")
print(f" Numer jaki podałeś to {number}")
if "0" in number:
    print(" Tak występuje tu zero ")
else:
    print("Nie nie ma tu zera")


# Utwórz zmienną value oraz instrukcję warunkową,
# która sprawdzi czy wartość tej zmiennej jest True, False, None czy te inną wartością

value =3

if value is True:
    print("Jest True")
elif value is False:
    print("Jest False")
elif value is None:
    print("Jest None")
else:
    print("Jest wartością inną")