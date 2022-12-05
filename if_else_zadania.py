#Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania

computer_price = float(input("Ile średnio kosztuje komputer?"))
car_price = float(input("Ile średnio kosztuje samocód?"))
bike_price = float(input("Ile kosztuje typowy rower?"))

if computer_price > car_price :
    print("Komputer jest droższy od samochodu")
else:
    print("Komputer jest tańszy od samochodu")

if bike_price < computer_price :
    print("Rower jest tańszy od komputera")
else:
    print("Rower jest droższy od komputera")

if car_price == bike_price :
    print("Samochód kosztuje tyle sami co rower")
else:
    print("Samochód nie kosztuje tyle samo co rower")

# Proszę o wpisanie listy zakupów
# rozdzielając poszczególne elementy przecinkiem
# Następnie powiedz (wpisz), czy jest to według Cienie długa lista czy też nie

shoping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shoping_elements = shoping_elements.split(",")

if len(shoping_elements) > 4:
    print("Ale długa lista zakupów")
else:
    print("Taka zwykła lista zakupów, nie za długa")

# =====================================
# Zapytaj użytkownika o jego oceny końcowe z kilku przedniotów (matematyki, fizyki, itd.).
# Następnie przeanalizuj je i wypisz informacje czy zdał/zdała do następnej klasy
# Załóż, że zdać można tylko jeżeli nie ma się żadnej jedynki
# albo jeżeli ma się jedną jedynkę ale średnia ocen ze wszystkich ocen jest wyższa niż 3.5

math_grade = int(input("Jaka jest Twoja ocena z matematyki? "))
physics_grade = int(input("Jaka jest Twoja ocena z fizyki? "))
polish_grade = int(input("Jaka jest Twoja ocena z polskiego? "))
english_grade = int(input("Jaka jest Twoja ocena z angielskiego? "))
history_grade = int(input("Jaka jest Twoja ocena z historii? "))

number_of_failures = 0

if math_grade < 2:
    number_of_failures = number_of_failures +1

if physics_grade < 2:
    number_of_failures = number_of_failures +1

if polish_grade < 2:
    number_of_failures = number_of_failures +1

if english_grade < 2:
    number_of_failures = number_of_failures +1

if history_grade < 2:
    number_of_failures = number_of_failures +1

suma = float(math_grade + physics_grade + polish_grade + english_grade + history_grade) / 5
if number_of_failures == 0:
    print("Gratulacje zdałeś....")
    if number_of_failures > 1:
        print("Niestety....")
    else:
        if number_of_failures == 1:

            if suma > 3.5:
                print("Zdałeś")
            else:
                print("Niestety..")
    print(f"Twoja średnia to {suma}")


