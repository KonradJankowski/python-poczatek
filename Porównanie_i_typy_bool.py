# Porównanie wykonujemy za pomocą operatorów mniejszości, większości, tip
apple_price = 3
bananas_price = 4.5
pears_price = 3

print(f"Czy jabłka są droższe od bananów? \t\t\t\t\t\t\t {apple_price > bananas_price}")
print(f"Czy jabłka są tańsze od bananów? \t\t\t\t\t\t\t {apple_price < bananas_price}")
print(f"Czy banany kosztują tyle samo co gruszki? \t\t\t\t\t {bananas_price == pears_price}")
print(f"Czy jabłka są droższe lub w tej samej cenie co gruszki? \t {apple_price >= pears_price}")
print(f"Czy jabłka mają tą samą cenę co gruszki? \t\t\t\t\t {apple_price == pears_price}")

#Jakiego typu jest wynik porównania?
result = apple_price > bananas_price
print("wynik porównania jest typem: ", type(result))

result = bool(7)
print(f" bool(7) -> {result}")
result = bool(-3.4)
print(f"bool(-3.4) -> {result}")
result = bool(0)
print(f"bool(0) -> {result}")

result = bool("Napis")
print(f"bool('Napis') -> {result}")
result = bool('')
print( f"bool('') -> {result}")
result = bool("")
print( f'bool("") -> {result}')

#Możemy porównywać napisy
name = "Konrad"
result = name == "Konrad"
print(f"name == 'Konrad' -> {result}")

your_name = input("Jak masz na Imię? ")
are_your_name_Konrad = your_name == "Konrad"
print(f"Twoje imię to Konrad? {are_your_name_Konrad}")

# Porównanie dwóch wartości napisów - w przypadku napisów bierze kolejność liter w alfabecie
print(f"Warzywa > Słodycze -> {'Warzywa' > 'Słodycze'}")