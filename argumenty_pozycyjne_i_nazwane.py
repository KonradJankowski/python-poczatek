# Wywołuj funkcję z zastosowaniem argumentów nazwanych

def average(distance, time):
    return distance / time


def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonałeś/pokonałaś za pomocą {vehicle_name}? "))
    time = float(input("Ile czasu Ci to zajęło? "))
    average_speed = average(distance=distance, time=time)
    print(f" Twoja średnia prędkość za pomocą {vehicle_name} to: {average_speed:.2f} km/h ")


run_avg_speed_calculator(vehicle_name="biegu")
run_avg_speed_calculator(vehicle_name="roweru")
run_avg_speed_calculator(vehicle_name="samochodu")