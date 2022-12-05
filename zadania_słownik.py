szkoła = {
    "informatyka": 6,
    "polski": 3,
    "geografia": 4
}

print(szkoła)

my_family = {
    "ja": {
        "first_name": "Konrad",
        "last_name": "Jankowski",
        "age": 36
    },
    "żona": {
        "first_name": "Kamila",
        "last_name": "Jankowska",
        "age": 36
    },
    "syn": {
        "first_name": "Aleksander",
        "last_name": "Jankowski",
        "age": 12
    },
    "córka": {
        "first_name": "Alicja",
        "last_name": "Jankowska",
        "age": 7
    }
}

print(my_family)




wydatki = {
    "jedzenie" : int(input("napisz ile miesięcznie wydajesz na jedzenie: ")),
    "rozrywka" : int(input("napisz ile miesiećznie wydajesz na rozrywkę: ")),
    "opłaty" : int(input("napisz ile miesiecznie wydajesz na opłaty: ")),
    "inne" : int(input("napisz ile miesięcznie wydajesz na inne cele: "))
}
suma = sum(wydatki.values())
wydatki["suma"] = suma
print(suma)
print(wydatki)
