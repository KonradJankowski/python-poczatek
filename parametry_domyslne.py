# Wartość domyślna

def best_grades(grades, best_grades_number=1):
    grades.sort(reverse=True)
    if best_grades_number < len(grades):
        return grades[:best_grades_number]
    print("Nie można zwrócić więcej ocen niż jest na liście. Zostaną zwrócone wszystkie")


math_grades = [1, 3, 4, 1, 2, 5, 4]
print(best_grades(math_grades))
print(best_grades(math_grades, 4))
print(best_grades(math_grades, best_grades_number=4))

# Uwaga! Jeżeli jako domyślnego argumentu chcemy użyć listy lub słownika
# Należy to zrobić w ten sposób
def write_final_grade(subject_grades, final_grades=None):
    if final_grades is None:
        final_grades = []
    grades_avg = sum(subject_grades) / len(subject_grades)
    final_grades.append(int(grades_avg))
    return final_grades

# # UWAGA! TAK JEST ŹLE!
# def write_final_grade(subject_grades, final_grades=[]):
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades

## UWAGA! Jeżeli jako domyślnego argumentu chcemy użyć listy lub słownika
# Należy to zrobić w ten sposób
def do_something_with_defoult_dic(something=None):
    if something is None:
        something = {}
    print("Tutaj dalsza implementacja...")