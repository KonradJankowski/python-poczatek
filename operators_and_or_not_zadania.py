income = float(input("Jaki jest miesięczny przychód Twojej firmy?"))
number_of_employees = int(input("Ilu pracowników zxatrudniasz? "))
suppot_answear = input("Czy Twoja firma otrzymała juz jakieś wsparcie wcześniej ? (T/N)")

if suppot_answear == "T":
    suppot_used = True
else:
    suppot_used = False

if (income < 15500 or (number_of_employees >= 3 and income < 30000 ) )and (not suppot_used) :
    print(f"Możesz otrzymać dotację")
else:
    print("Niestety nie otrzymasz dotacji")

#============================================================================

income = 4000
expenditures = 2000
age = 36

if age < 18 or income < expenditures:
    print("Nie możesz wziąść kredytu")
else:
    print("Możesz wziąść kredyt")

if not (age < 18 or income < expenditures):
    print("Możesz wziąść kredyt")
else:
    print("Nie możesz wziąść kredytu")