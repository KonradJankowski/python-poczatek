# Mamy 4 rodzaje wsparcia - od najlepszych do najgorszych śa to:
# - Główne wsparcie -> przychód poniżej 5000
# - Wsparcie z funduszu pracowników -> od 5 do 10 pracowników
# - Wsparcie dla nowych firm -> krócej niz 3 lata na rynku
# - Wsparcie na pocieszenie -> dla każdego kto nie dostał żadnego innego

income = 42000
employees_number = 27
years_on_the_market = 3

# if income  < 5000:
#     print("Przyznano główne wsparcie")
# else:
#     if 5 <= employees_number <= 10 :
#         print("Przyznano wsprarcie z funduszu pracowników")
#     else:
#         if years_on_the_market < 3:
#             print("Przyznano wsparcie dla nowych firm")
#         else:
#             print("Przyznano wsparcie na pocieszenie")
# Refactor:

#============================
# Instrukcja elif pozwala powiedziec "inaczej, jeśli....."

if income < 5000:
    print("Przyznano główne wsparcie")
elif 5 <= employees_number <= 10 :
    print("Przyznano wsparcie z funduszu pracowników")
elif years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm")
else:
    print("Przyznano wsparcie na pocieszenie")
