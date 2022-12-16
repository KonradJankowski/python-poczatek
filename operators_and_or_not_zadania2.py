# Napisz uproszczony kalkulator kredytowy. Celem kalkulatora jest
# sprawdzenie czy użytkownika stać na kredyt hipoteczny o podanych
# parametrach. Zapytaj użytkownika o: kwotę kredytu, oprocentowanie
# kredytu, wartość wkładu własnego, czas kredytowania w latach,
# przychód miesięczny, sumę miesięcznych wydatków
#
# - Jeżeli wartość wkładu wkładu własnegy to powyżej 20% wartości
# nieruchomości to dostępne środki muszą być wyższe od raty ninimum
# o 1000PLN

# wzór
# (kwota kredytu * oprocentowanie / 100) / 12 + kwota kredytu / (liczba lat *12)
#
# Oblicz dostępne środki jako: przychód - suma wydatków
#
# Oblicz wartość nieruchomości jako:
# wkład własny + kwota kredytu

loan_amount = int(input("O jaką kwotę kredytu wnioskujesz? "))
interest_rate = float(input("Podaj oprocentowanie?"))
own_contribution = int(input("Podaj jaki posiadasz wkład własny? "))
years = int(input("Jaki czas kredytowania (w latach) ? "))
monthly_income = int(input("Jaki jest miesięczny przychód? "))
monthly_expenditures = int(input("Jaka jest suma Twoich miesięcznych wydatków? "))

install_value = (loan_amount * interest_rate / 100) / 12 + (loan_amount / (years * 12))
available_money = monthly_income - monthly_expenditures
property_value = loan_amount + own_contribution

own_contribution_part = own_contribution / property_value
money_over_installment = available_money - install_value

matching_higher_own_part = own_contribution_part >= 0.2 and money_over_installment >= 1000
matching_lower_own_part = own_contribution_part >= 0.1 and money_over_installment >= 2000

if matching_lower_own_part or matching_higher_own_part:
    print("Możesz kredyt")
else:
    print("Nie możesz kredytu")
    