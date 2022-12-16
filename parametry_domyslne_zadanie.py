# Napisz funkcję, która podaną liczbę zamieni na zakres.
# Domyślnie przyjmujemy zakres jako +/- 10% podanej wartości.

def liczba(value, tolerance_percentage=10):
    tolerance_percentage = tolerance_percentage * value / 100
    return [value - tolerance_percentage, value + tolerance_percentage]

print(liczba(100))
print(liczba(100, tolerance_percentage=40))


# Napisz funkcję, dodającą kolejne osoby do listy osób uczęszczających na zajęcia.
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem oraz listę już zapisanych osób, która domyślnie jest pusta.
def add_people_to_class(names_str, particioants=None):
    if particioants is None:
        particioants = []
    names = names_str.split(',')
    for name in names:
        particioants.append(name)
    # participants += names
    return particioants

attends_names = "Olo, Ola, Kuba, Konrad"
monday_course_particioants = add_people_to_class(attends_names)
print(monday_course_particioants)
attends_names = "Alicja,Aleksander"
monday_course_particioants = add_people_to_class(attends_names, particioants=monday_course_particioants)
print(monday_course_particioants)

attends_names = "Kamila,Kamil"
friday_course_participants = add_people_to_class(attends_names)
print(friday_course_participants)