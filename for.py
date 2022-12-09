# składnia for

#   for <jakiś element >  in  <jakaś kolekcja może być lista, naopis, ..> :

collection = ["ciastko", "książka", "piłka"]

for element in collection:
    print(element)

# Wypisywanie listy ulubionych sportów
print("###########################")
favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
for sport in favourite_sports:
    print(sport)


print("###########################")
# Kod pocztowy po znaku

post_code = input("Podaj kod pocztowy: ")
for char in post_code:
    print(char)

print("###########################")

# Za pomocą pętli for możemy wypisać klucze ze słownika

expenditures = {
    "prąd": [250],
    "woda": [30.45],
    "zakupy": [
        120.15,
        117.53,
        20.15
    ]
}

for element in expenditures:
    print(element)


print("###########################")

# Klucze i wartości

for element in expenditures:
    print(f" klucz -> {element} i jego wartość {expenditures[element]}")

print("###########################")

# Same wartości

for element in expenditures.values():
    print(element)

print("###########################")

# Metoda Items zwaraca na słowniku krotki dwuelementowe, które zawierają klucz i wartość

for item in expenditures.items():
    print(item)
    print(f"{item[0]} -> {item[1]}")
    print(type(item))