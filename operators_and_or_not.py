name = input("Jak masz na imię? ")
print(f"Miło Cię poznać {name}")
name_lenght = len(name)

if name_lenght < 5:
    print(f"{name} to raczej krótkie imię")
if name_lenght >=5:
    if name_lenght <= 5 and name_lenght <=8:
        print(f"{name} to imię zwykłej długości!")
    else:
        print(f"{name} to długie imię")


#=============================================================================

born_as_usa_citizen_answear = input("Czy jesteś obywatelem USA od urodzenia ? (T/N) ")
age = int(input("Ile masz lat? "))
usa_residence_years = int(input("Ile lat mieszkasz w USA? "))

if born_as_usa_citizen_answear == "T":
    born_as_usa_citizen = True
else:
    born_as_usa_citizen = False

if born_as_usa_citizen:
    if age >= 35:
        if usa_residence_years >= 14:
            print("Możesz kandydować")
        else:
            print("Nie możesz kandydować")
    else:
        print("Nie możesz kandydować")
else:
    print("Nie możesz kandydować")