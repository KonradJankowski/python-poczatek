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