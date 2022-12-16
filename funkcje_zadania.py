# Napisz funkcję, która obliczy pole powierzchni prostokąta na podstawie długości jego boków.

def rectangle(a,b):
    return a * b


a = int(input("Podaj długość pierwszego boku: "))
b = int(input("Podaj długość drugiego boku: "))
area = rectangle(a, b)

print(f"Pole powierzchni prostokątu to {area}")

# Napisz funkcję liczącą prędkość średnią na podstawie zadanego dystansu i czasu.
# Następnie wykorzystaj ją implementując program, który wyznaczy:
# - średnią prędkość biegu
# - średnią prędkość jazdy na rowerze
# - średnią prędkość jazdy autem

def average(distance, time):
    return distance / time

#
# running_distance = float(input("Ile km przebiegłeś/przebiegłaś? "))
# running_time = float(input("Ile godzin Ci to zajęło? "))
# bike_ride_distance = float(input("Ile km przejechałeś/przejechałaś na rowerze? "))
# bike_ride_time = float(input("Ile godzin Ci to zajęło? "))
# car_drive_distance = float(input("Ile km przejechałaś/przejechałeś autem"))
# car_drive_time = float(input("Ile godzin Ci to zajęło? "))

def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonałeś/pokonałaś za pomocą {vehicle_name}? "))
    time = float(input("Ile czasu Ci to zajęło? "))
    average_speed = average(distance, time)
    print(f" Twoja średnia prędkość za pomocą {vehicle_name} to: {average_speed:.2f} km/h ")

run_avg_speed_calculator("biegu")
run_avg_speed_calculator("roweru")
run_avg_speed_calculator("samochodu")

# print(f"Twoja średnia prędkosć biegu to {average(running_distance, running_time)} km/h")
# print(f"Twoja średnia prędkość jazdy na rowerze to {average(bike_ride_distance, bike_ride_time)} km/h")
# print(f"Twoja średnia prędkosć jazdy na samochodem to {average(car_drive_distance, car_drive_time):.2f} km/h")
