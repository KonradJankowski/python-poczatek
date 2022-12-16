# Zmienna result została zdefiniowana wewnątrz funcji i nie mamy do niej dostępu spoza niej

def avg_speed(distance, time):
    result = distance, time
    print("Nic nie zwracam")

avg_speed(30, 2)
#print(result) # nie będzie działać!!

# Zmienna distance została zdefiniowana poza jakąkolwiek funcją - jest globalna
def avg_speed2(time2):
    result2 = distance2 / time2
    return result2

distance2 = 20
time_in_hours = 2
print(avg_speed2(time_in_hours))

# Próby zmiany wartości zmeinnych
def failed_modify_globl_name():
    name = "Kamila"
    print(f"Wewnątrz funkcji : {name}")

name = "Konrad"
print(f"Przed funkcją {name}")
failed_modify_globl_name()
print(f"Po funkcji: {name}")

def success_modify_global_name():
    global name
    name = "Kamila"
    print(f"Wewnątrz funkcji: {name}")

name = "Konrad"
print(f"Przed funkcją {name}")
success_modify_global_name()
print(f"Po funkcji: {name}")

