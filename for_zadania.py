# Poproś użytkownika o wprowadzenie ocen, które uzyskał/a.
#
# Wykorzystaj pętlę while, aby pytać o kolejne oceny i zakończyć wprowadzanie odpowiednim znakiem (np. X).
#
# Następnie, stosując pętlę for oblicz średnią z podanych ocen.
grade = 0
list = ""
while grade != "X":
    grade = input("Podaj ocene: ")
    if grade != "X":
        list += grade
suma = 0
#print(f"Oceny które wpisałem to: {list}")
for index in list:
    ocena = int(index)
    suma = suma + ocena
#    print(f"Składniowa sumy {suma}")
#print(type(ocena))
#rint(type(suma))
srednia = suma / (len(list) )
print(f"Tyle wynosi suma: {suma}")
print(f"Dłogość listy to: {len(list)}")
print(f"Tyle wynosi średnia: {srednia}")

print("========================================================================")

# Wczytaj od użytkownika kolejne kategorie wydatków oraz dla każdej z nich dokonane wydatki.
#
# Zastosuj pętlę while, aby użytkownik mógł zakończyć wprowadzanie kategorii i wydatków.
#
# Stosując pętlę for oblicz procentowy udział każdego z wydatków w miesięcznym budżecie i wypisz wyniki oraz
# dodatkową informację,
# która powie o najbardziej znaczącej kategorii.

expenditures = {}

category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'x' : ")
while category_name != 'x':
    expenditures[category_name] = []
    expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ 'x'")
    while expenditure != 'x':
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)
        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ 'x'")
    category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'x'")

total_expenditures = 0
for category_expenditures in expenditures.values():
    for expenditure_value in category_expenditures:
        total_expenditures += expenditure_value

expenditures_percentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditures = 0
    for expenditure_value in category_expenditures:
        total_category_expenditures += expenditure_value
    expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures

most_important_category = None
most_important_category_percentage = 0
for category, percentage in expenditures_percentage.items():
    if percentage > most_important_category_percentage:
        most_important_category_percentage = percentage
        most_important_category = category

if most_important_category is not None:
    print(f"Najwięcej wydasz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków ")

for category, percentage in expenditures_percentage.items():
    print(f"Na {category} wydajesz {percentage:.0f}% miesiecznie")