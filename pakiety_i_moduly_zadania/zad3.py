# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
#
# Wczytaj od użytkownika informacje o:
#  -> Początkowym kapitale (wpłaconej kwocie)
#  -> Oprocentowaniu
#  -> Okresie trwania inwestycji (w latach)

print(__name__)

import calculations.investment

def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value = ask_for_int_value("Jaką kwotę wpłaciłeś? ")
percent_age = ask_for_int_value("Jakie jest oprocentowanie? ")
years = ask_for_int_value("Ile trwa lokata? ")

final_value = calculations.investment.calculate_investment_value(initial_value,percent_age, years)
print(f"po {years} latach Twoja lokata będzie warta {final_value:.2f}")