# Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i pokonanego dystansu (prędkość = dystans / czas)
# i umieść ją w jednym pliku.
# W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika i wywołaj funkcję - oblicz prędkość średnią.

import speed_calculator

running_distance = float(input("Ile km przebiegłeś? "))
running_time = float(input("Ile godzin Ci to zajęło? "))

avg_speed = speed_calculator.avg_speed(running_distance, running_time)
print(f"Twoja średnia prędkość biegu to {avg_speed} km/h")