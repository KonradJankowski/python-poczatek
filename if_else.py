# Instrukcja warunkowa if jest bardzo czytelna
if 7 > 3:
    print("To jest oczywiste!")

if 10 < 4:
    print("To niegdy się nie zdarzy")

# If w połączeniu z dynamicznymi (np. wprowadzonymi przez użytkownika) danymi
name = input("Jak się nazywasz? ")
print(f"Miło Cię poznać {name}")
print("Miło Cię poznać ",name)
if len(name) >= 7:
    print(f"{name} to całkiem długie imię")
if len(name) < 7:
    print(f"{name} to raczej krótkie imię")

age = int(input("Ile masz lat? "))
if age < 18:
    print("Jeszcze nie możesz głosować")
if age >= 18:
    print("Możesz juz głosować!")
if age >= 21:
    print("Możesz kandydować na posła")
if age >= 30:
    print("Możesz kandydować na senatora")
if age >= 35:
    print("Możesz kandydować na prezydenta")

#=============if=============else===================
# Przykład z if wzbogacone o instrukcję else
if 7 > 3:
    print("To oczywiste! ")
else:
    print("To się nie wydaży")

name = input("Jak się nazywasz? ")
print(f"Miło Cię poznać {name}")
if len(name) >= 7:
    print(f"{name} to całkiem długie imię")
else:
    print(f"{name} to raczej krótkie imię")

age = int(input("Ile masz lat? "))
if age < 18:
    print("Jeszcze nie możesz głosować")
else:
    print("Możesz juz głosować!")
    if age >= 21:
        print("Możesz kandydować na posła")
    if age >= 30:
        print("Możesz kandydować na senatora")
    if age >= 35:
        print("Możesz kandydować na prezydenta")