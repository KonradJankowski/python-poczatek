name = input("Jak masz na imię? ")
print(f"Miło Cię poznać {name}")
name_lenght = len(name)

if name_lenght < 5:
    print(f"{name} to raczej krótkie imię")
if name_lenght >=5:
    if name_lenght <= 8:
        print(f"{name} to imię zwykłej długości!")
    else:
        print(f"{name} to długie imię")