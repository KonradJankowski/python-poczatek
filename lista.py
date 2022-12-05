# Lista zakupów
shopping_list = [
    "chleb",
    "mąka",
    "jabłka",
    "pomarańcze",
    "kawa",
    "czekolada",
    "ser",
    "jogurty"
    "masło",
    "dzem"
]

print("Lista zakupów: ",shopping_list)

empty = []
print("Pusta lista: ", empty)

favorite_flavours = [
    "malinowy",     #0 / -5
    "truskawkowy",  #1 / -4
    "czekoladowy",  #2 / -3
    "pistacjowy",   #3 / -2
    "kokosowy",     #4 / -1
    ]
print("\n\n\nLista smaków: ", favorite_flavours, "\n")
print("Ulubiony smak moich lodów to: ", favorite_flavours[3])
print("Drugi ulubiony smak moich lodów to: ", favorite_flavours[1])
print("Długość listy to: ", len(favorite_flavours), "smaków")
print("Ostatni element na liście to: ", favorite_flavours[len(favorite_flavours) -1])
print("Elementy listy mniejsze niż dwa: ", favorite_flavours[:2])
print("Elementy listy większe i równe niż dwa: ", favorite_flavours[2:])
print("\n===========================================================\n")
print("\n===========================================================\n")
