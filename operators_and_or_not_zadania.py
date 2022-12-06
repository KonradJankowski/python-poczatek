income = float(input("Jaki jest miesięczny przychód Twojej firmy?"))
number_of_employees = int(input("Ilu pracowników zxatrudniasz? "))
suppot_answear = input("Czy Twoja firma otrzymała juz jakieś wsparcie wcześniej ? (T/N)")

if suppot_answear == "T":
    suppot_used = True
else:
    suppot_used = False

if income < 15500 or (number_of_employees >= 3 and income < 30000 ) or (suppot_used not True) :
    print(f"Możesz otrzymać dotację")
else:
    print("Niestety nie otrzymasz dotacji")