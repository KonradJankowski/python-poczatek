polish_to_english = {
    "amnezja" : "amnesia",
    "aktywista" : "activist",
    "burza" : "storm",
    "mgła" : "wist" ,
    "lista" : ["lista1", "lista2"]
}
print(polish_to_english)
print(polish_to_english["lista"][1])
print(polish_to_english.keys())
print(polish_to_english.values())

students = [
    {
        "first_name" : "Konrad",
        "last_name" : "Jankowski"
    },
    {
        "first_name" : "Aleksander",
        "last_name" : "Jankowski"
    }
]

print(students)



print(students)
print(students[0])
print(students[1])
print(students[1]["first_name"])
polish_to_english["chusteczki"] = "wipes"
print(polish_to_english)
del polish_to_english["burza"]
print(polish_to_english)
słowo = polish_to_english.pop("mgła")
print(słowo)