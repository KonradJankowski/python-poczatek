# Poszukiwanie elementu w zbiorze
expenditures = [120, 300, 250.45, 1300, 50, 75]

for expenditure in expenditures:
    print(expenditure)
    if expenditure > 1000:
        print("Drogi wydatek znaleziony")
        break


print("=============================================================")

# Pętla for posiada również opcjonalną część "else"
for expenditure in expenditures:
    if expenditure > 1000:
        print("Drogi wydatek znaleziony ")
        break
else: # Wykona się jeżeli pętla wykona się normalnie a nie przez break
    print("Nie znaleziono wydatku")

print("=============================================================")

# Break do przerywania wprowadzania informacji od użytkownika
grades = []
while True:
    grade_input = input("Podaj kolejną ocenę albo zakończ wpisująć 'X'")
    if grade_input == "X":
        break
    grade = int(grade_input)
    grades.append(grade)

grades_sum = sum(grades)
average = grades_sum / len(grades)
print(f"Twoja średnia wynosi: {average:.2f}")

print("=============================================================")

# Również pętla while ma opcjonalnego else`a
grades = []
while len(grades) < 5:
    grade_input = input("Podaj kolejną ocenę albo zakończ wpsiując 'X'")
    if grade_input == 'X':
        break
    grade = int(grade_input)
    grades.append(grade)
else:
    print("Wystarczy tych ocen")