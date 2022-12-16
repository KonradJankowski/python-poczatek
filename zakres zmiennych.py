# Zmienna result została zdefiniowana wewnątrz funkcji i nie mamy do niej dostępu spoza niej

tekst = "zmienna zdefiniowana na początku"

def avg_speed(distance, time):
    result = distance / time
    #Zakres zmiennej zdefiniowanej wewnątrz funkcji jest lokalny, tzn
    #ogranicza się do kodu wewnątrz funkcji
    print("Nic nie zwracam - ha ha ha ha !")
    print(tekst) # ta zmienna została zdefiniowana na zewnątrz funkcji - zmienna globalna
                 # bo zdefiniowana jest na poziomie skryptu



avg_speed(30, 2)
#print(result)    to nie zadziała bo zmienna została zdefiniowana w funkcji avg_speed()



#|-------------Buildin-------------|     np. int() i inne już zdefiniowane takie oczywiste oczywistości
#||------------Global-------------||
#|||-------Enclosing(nonlocal)---|||     np. gdy zdefiniujemy sobie jedną funkcję wewnątrz drugiej funkcji
#||||-----------Local-----------||||
#|||-----------------------------|||
#||-------------------------------||
#|---------------------------------|

# zmienne wew funkcji mogą się nazywac jak na zewnątrz funkcji i mówimy wtedy o przysłonięcie wartości
# nie zmieniamy wtedy zmiennej globalnej tylko tworymy nową zmienną wewnatrz funkcji która się tak samo
# nazywa le nie jest zmienną globalną

# aby wewnątrz funcji zmienić zmienną globalną używamy słowa global


capital = 1
def some_func():
    capital =2
    print(capital)

def oteher_func():
    global capital
    capital = 3 # zmienia zmienną globalną na 3 / nadpisujemy
    print(capital)

print(capital)
some_func()
oteher_func()
print(capital)

# dobra praktyka:
# - Ograniczyć stosowanie zmiennych globalnych
# - Nie "Przesłaniać zmiennych (różne nazwy)
# - Nie używać global
