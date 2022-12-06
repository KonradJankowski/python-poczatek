income = float(input("Jaki jest miesięczny przychód Twojej firmy?"))
number_of_employees = int(input("Ilu pracowników zxatrudniasz? "))

if income < 15500 or (number_of_employees >= 3 and income < 30000 ):
    print(f"Możesz otrzymać dotację")
else:
    print("Niestety nie otrzymasz dotacji")