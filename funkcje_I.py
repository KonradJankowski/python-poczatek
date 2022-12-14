# Obieranie ziemniaków - definicja funkcji
def peel_the_potatoes():
    expected_potatoes = int(input("Ile ziemniaków chcesz na obiad ? "))
    potatoes = []
    while len(potatoes) < expected_potatoes:
        print("Obieram ziwmniaka..")
        print("I wrzucam go do garnka :")
        potatoes.append("Ziemniak")
    print(potatoes)

# Obieranie ziemniaków - wywołanie funkcji
peel_the_potatoes()
# peel_the_potatoes()
# peel_the_potatoes()

def put_a_brick():
    print("-", sep="", end="")

#Funkcja może wołać inną funkcję
def build_a_wall():
    wall_lenght = 10
    for brick in range(wall_lenght):
        put_a_brick()
    print()

build_a_wall()

# Funkcja moze przyjmować parametry - widoczne wewnątrz jako zmienne
def function_with_params(something, something_else):
    print(something)
    print(something_else)

function_with_params(1, 4)
function_with_params("Napis", 4)

print("========================")

def build_a_wall(wall_lenght):
    for brick in range(wall_lenght):
        put_a_brick()
    print()

build_a_wall(5)
build_a_wall(10)

# Zwaracanie z funkcji
def say_hello():
    print("Hello World!")
    # w domyśle ma return None

hello_result = say_hello()
print(hello_result)

################Ale mozemu zwrócić wynik

def say_hello():
    print("Hello World!")
    return "say_hello"
hello_result = say_hello()
print(hello_result)




