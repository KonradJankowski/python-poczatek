# Poproś użytkownika o wprowadzenie ocen, które uzyskał/a.
#
# Wykorzystaj pętlę while, aby pytać o kolejne oceny i zakończyć wprowadzanie odpowiednim znakiem (np. X).
#
# Następnie, stosując pętlę for oblicz średnią z podanych ocen.
grade = 0
list = ""
while grade != "X":
    grade = input("Podaj ocene: ")
    if grade != "X":
        list += grade
suma = 0
print(f"Oceny które wpisałem to: {list}")
for index in list:
    ocena = int(index)
    suma = suma + ocena
    print(f"Składniowa sumy {suma}")
print(type(ocena))
print(type(suma))
srednia = suma / (len(list) )
print(f"Tyle wynosi suma: {suma}")
print(f"Dłogość listy to: {len(list)}")
print(f"Tyle wynosi średnia: {srednia}")