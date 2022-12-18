# Bibliotek standardowa zawiera wiele przydatnych narzędzi
import math

# Stała PI
print('pi', math.pi)

# Funkcja sinus
sinus_180 = math.sin(math.pi)
print('sinus_180', sinus_180)

# Nieskończoność
print('math.inf', math.inf)

# Zapis z dowolnym podkreśleniem jest równoznaczny temu "bez" - tylko czytelność
very_big_number = 100_000_000_000_000
the_bigger_number = math.inf

# Nieskończonośc jest większa niż cokolwiek innego
print('the_bigest_number: ', the_bigger_number > very_big_number)

# Pakiet to specjalny rodzaj modułu