# Instrukcja in pozwala sprawdzić czy litera wystepuje w napisie

name = "Konrad"
if "o" in name:
    print("W imieniu jest 'o'")
else:
    print("W imieniu nie ma o")



# Możemy sprawdzić czy element występuje na liście

favourite_sports = ["bieganie", "jazda na rowerze", "pływanie"]

if "koszykówka" in favourite_sports:
    print("Zagramy w kosza?")
else:
    print("Nie ma")


# Sprawdzenie czy występuje klucz w słowniku

person = {
    "first_name": "Konrad",
    "last_name": "Jankowski",
}
if "first_name" in person:
    print(person["first_name"],person["last_name"])


#=======================================================
##
##                   is                               ##
##
#=======================================================

age = 36

if age:
    print("if age")

if age == True:
    print("age == True")

if age is True:
    print("if age is True")

true_value = True
if true_value is True:
    print("if true_value is True")

nothing = None
if not nothing:
    print("if not nothing")

zero = 0
if not zero:
    print("if not zero")

if zero is None:
    print("if nothing is None")

if nothing is None:
    print("if nothing is None")

if zero is not None:
    print("if zero is not None")

if nothing is not None:
    print("if nothing is not None")
