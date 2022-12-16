# Poproś użytkownika o podanie numeru telefonu.
#
# Następnie wypisz informację ile razy występuje w nim każda cyfra.

number = input("Podaj numer telefonu: ")

for digit in range(10):
    digit_times_in_number = number.count(str(digit))
    print(f"Cyfra {digit} występuje {digit_times_in_number}")