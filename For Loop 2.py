scores = {
    "Alfred": {
        "Maths": 74,
        "Science": 78,
        "English": 68,
        "History": 52
    },
    "Matthew": {
        "Maths": 64,
        "Science": 82,
        "English": 70,
        "History": 65,
        "Psychology": 87
    },
    "Simon": {
        "Maths": 61,
        "Science": 63,
        "English": 71,
        "History": 56
    },
    "Amy": {
        "Maths": 91,
        "Science": 89,
        "English": 69,
        "History": 71
    },
    "Mary": {
        "Maths": 53,
        "Science": 74,
        "English": 90,
        "History": 85,
        "Psychology": 75
    },
}

# for student in scores:
#     print("\n" + student)
#     for topic in scores[student]:
#         print(scores[student][topic])
#         #for marks in scores[student][topic]:
#             #print(marks)



# print(scores["Mary"])
# print(scores["Mary"]["Maths"])

for studentName in scores:
    print("\nLevel 1 Key: " + studentName) # Looks at the scores dict., pulls the KEY.
    print("Level 1 Value: ")
    print(scores[studentName])  # Looks at the scores dict, pulls KEY
    for subjectName in scores[studentName]: # Taking into account the in statement: Goes into the Scores - Student dict. and names the KEY subjectName.
        print("Level 2 Key: " + subjectName) # Pulls subject name from the previously set 2nd level dict.
        print("Level 2 Value: " + str(scores[studentName][subjectName])) # Level 2 key, pulls level 2 value.

orders = {
    "Josh": {
        "Fajitas": 3.60,
        "Banana": 0.75,
        "Ribena": 1.20
    },
    "Omar": {
        "Tuna Sandwich": 2.50,
        "Crisps": 0.80,
        "Water": 0.99
    },
    "Justyna": {
        "Stir Fry": 4.75,
        "Pringles": 1.10,
        "Green Tea": 1.35
    },
    "Oliver": {
        "Bolognése": 15.00,
        "Old Fashioned": 8.50,
        "Ciabatta": 3.20

for customerName in orders:
    print(customerName)
    total = 0
    for item in orders[customerName]:
        total += orders[customerName][item]
    print("£",total)
