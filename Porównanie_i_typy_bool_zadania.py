first_price = input("Podaj pierwszącenę za produkt: ")
second_price = input("Podaj drugą cenę za produkt: ")
third_price = input("Podaj trzecią cenę za produkt: ")

print(f"Czy pierwsza cena jest większa od trzeciej? \t\t {first_price > third_price}")
print(f"Czy druga cena jest równa trzeciej ? \t\t\t\t  {second_price == third_price}")
print(f"Czy trzecia cena jest mniejsza lub równa pierwszej? \t {third_price <= first_price}")

# Proszę o wpisanie listy zakupów
# rozdzielając poszczególne elementy przecinkiem
# Następnie powiedz (wpisz), czy jest to według Cienie długa lista czy też nie

shoping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem: ")
shoping_elements = shoping_elements.split(",")

is_shopping_list_long = len(shoping_elements) > 4
print(f"Czy uważasz, że Twoja lista zakupów jest długa? {is_shopping_list_long}")

