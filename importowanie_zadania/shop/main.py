# Napisz prosty symulator sklepu.
# W jednym pliku zdefiniuj dostępne produkty: nazwę (np. chleb i jabłka), dostępną ilość i cenę jednostkową.
# W innym zaimplementuj funkcję, która na podstawie nazwy produktu i zamawianej ilości stworzy nowe zamówienie
# i doda je do listy zamówień. Zamówienie składa się z nazwy produktu, zamówionej ilości i łącznej ceny.
# Obydwa pliki umieść w pakiecie.
#
# Sklep uruchom poprzez plik main, w którym zaimportujesz funkcje do tworzenia zamówienia,
# wczytasz dane od użytkownika i wypiszesz łączny koszt zakupów.
# Zastosuj importowanie absolutne postaci from … import.

from shop.orders import create_new_order

print("Witaj w naszym sklepie!!")
product_name = input("Jaki towar chcesz kupić? ")
quantity = int(input("Ile sztuk/kg chcesz kupić? "))

result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result["total_price"]
    print(f"Łączny koszt wyniesie: {total_price} PLN")