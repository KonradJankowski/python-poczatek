# Zmodyfikuj rozwiązanie zadania z promocją do kolejnej klasy z lekcji o instrukcji if/else (moduł 4).
# Wczytaj oceny do listy.
# Jeżeli jest jakakolwiek jedynka to klasę trzeba powtórzyć.
# W przeciwnym razie należą się gratulacje.

subjects = ["matematyka", "fizyka", "język polski", "język angielski", "historia"]
grades = []

for subject in subjects:
    grade = int(input(f"Jaka jest Twoja ocena z przedniotu {subject} :"))
    grades.append(grade)

for grade in grades:
    if grade == 1:
        print("Niestety..")
        break
else:
    print("Gratulacje masz promocję do następnej klasy")

print("=======================================================================")

# Utwórz listę zawierającą różne liczby i skorzystaj z instrukcji continue aby wypisać tylko
# przerywa pętle i przechodzi do ponownego wykonania pętli z pominięciem co jest dalej po continue
numbers = [1, 3, 4 ,2, 3, 4, 56, 234, 2, 62, 523, 451, 34]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

