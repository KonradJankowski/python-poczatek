counter =0
while counter < 10:
    print(counter)
    counter +=1

# while True:
#     print("Nigdy nie skończę!!!")

expected_potatoes = int(input("Ile ziemniaków chcesz na obiad ? "))
potatoes = []
while len(potatoes) < expected_potatoes:
    print("Obieram ziemniaka...")
    print("I wrzucam do garnka")
    potatoes.append("Ziemniak")
print(potatoes)

#==========================
#Wypisywanie elementów listy

favourite_sports = ["bieganie", "pływanie", "jazda na rowerze", "triathlon"]
sport_index = 0
while sport_index < len(favourite_sports):
    print(favourite_sports[sport_index])
    sport_index += 1

#####################
# Sumowanie liczb
numbers = [1, 3, 510, 123, 24]
numbers_sum = 0
number_index = 0
while number_index < len(numbers):
    numbers_sum += numbers[number_index]
    number_index += 1
print(f"Suma: {number_index}")

#########################
print("\n")
print("\n")

#Zamieniamy kod pocztowy by zawsze był zgodny z formatem XX-XX-XX-XX-XX
post_code = str(input("Podaj kod pocztowy: "))
post_code = post_code.replace("-", "")
print(post_code)
post_code_formated = ""
letter_index = 0
while letter_index < len(post_code):
    if letter_index % 2 == 0 and letter_index != 0:
        post_code_formated += "-"
    post_code_formated += post_code[letter_index]
    letter_index += 1
print(post_code_formated)

