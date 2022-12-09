# Wypisujemy kod pocztowy - znak po znaku wraz z informacją o kolejności

post_code = input("Jaki jest Twój kod pocztowy? ")
for index, letter in enumerate(post_code):
    print(f"[{index}] -> {letter}")


print("####################################")
#Wypisywanie co drugiego sportu
favorite_sports = ["Bieganie", "pływanie", "jazda na rowerze", "rolki", "ping pong", "tenis"]
for index, sport in enumerate(favorite_sports):
    if index % 2 == 0:
        print(f"[{index}] -> {sport}")