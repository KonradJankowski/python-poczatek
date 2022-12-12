# Wypisywanie co drugiego sportu
favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "spacerowanie"]
for index, sport in enumerate(favourite_sports):
    if index % 2 != 0:
        continue #działa w podobny sposób do breaka,
        # nie powoduje całkowitego rzerwania pętli a przerwanie pozostałych do wykonania instrukcji
        # dla aktualnego jej przebiegu
    print(sport)