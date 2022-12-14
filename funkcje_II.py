def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    return result


def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)


print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value = ask_for_int_value("Jaką kwotę wpłąciłeś/wpłaciłaś? ")
percentage = ask_for_int_value("Jakie jest oprocentowanie (%)? ")
years = ask_for_int_value("Ile lat trwa lokata? ")

final_value = calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latach Twoja lokata bedzie warta {final_value}")

long_term = years * 2
alternative_value = calculate_investment_value(initial_value, percentage, long_term)
print(f"Rozważ zostawienie lokaty na {long_term} lat - będzie warta {alternative_value}")
