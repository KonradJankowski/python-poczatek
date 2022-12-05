# years = input("Hej, podaj ile masz lat? : ")
# months = 12 * int(years)
#
# print("W przeliczeniu to na pełne miesiące jest to : ", months )
#
# print("====================================================\n\t========================================")
# weeks = input("Ile przeszedłeś w tym tygodniu km? : ")
# distance = 40075 / int(weeks)
# print("Przejście całej ziemi w tym tempie zajęło by Ci: ", distance, " tygodni")
# print("====================================================\n\t========================================")


print("Obliczamy teraz lokatę")
star_value=input("Podaj wartość początkową: ")
star_value_int = int(star_value)
oprocentowanie = input(" podaj w procentach oprocentowanie: ")
oprocentowanie_int = int(oprocentowanie)
time = input("Podaj czas trwania lokaty w latach: ")
tine_int = int(time)

wartość = star_value_int * (1 + oprocentowanie_int/100) ** tine_int
wartość = float(wartość)

print(f"Wartosć oprocentowania to:  {wartość:.2f} ")