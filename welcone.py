# Importujemy moduł hello - jest on dostepny w tym pliku
import hello

# Za pomocą kropki mozemy się odwołać do funkcji i zmiennych dostępnych w hello
hello.say_hello()
name = input("Jak się nazywasz? ")
hello.say_hello_with_name(name)