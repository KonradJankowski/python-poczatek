<<<<<<< HEAD
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
=======
# Agrumenty pozycyjne
def add_two_number(first_num, second_num):
    print(f"first_num: {first_num}")
    print(f"second_num: {second_num}")
    return first_num + second_num

print(add_two_number(2, 5))
print(add_two_number(5, 2))

# Nie możemy pomylić kolejności
def calculate_investment_value(initial_value, percenage, years):
    result = initial_value * (1 + percenage / 100) ** years
    return result


initial = 1000
percentage = 5
years = 4

#Nie poprawene użycie argumentów do wzoru - błędne przekazywanie
final_value = calculate_investment_value(percentage, years, initial)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

#Poprawne użycie argumentów do wzoru
final_value = calculate_investment_value(1000, 5, 4)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

#Inne wywołanie - większa czytelność - jawne przekazywanie parametru
final_value = calculate_investment_value(initial_value=1000, percenage=5, years=4)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

# Możemy przekazywać argumenty w dowolnej kolejności - o ile je nazwiemy lecz nie polecane
final_value = calculate_investment_value(percenage=5, years=4, initial_value=1000)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

###########################################
#Wszystkie argumenty pozycyjne muszą pojawić się przed argumentami nazwanymi !!! jeżeli mieszamy
>>>>>>> funkcje
