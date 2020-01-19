#x = 0

#while (x) < 10:
#    print(x)
#    x += 1 # x = x + 1

#while x <= 10:
#    print(f"The number is currently {x}")
#    x += 1 # x = x + 1
 #   if x == 4:
  #      print("bored now")
   #     break

counter = 0

ageNum = False
while ageNum == False:
    counter += 1
    age = input(f"Attempt {counter}: What is your age?\n")
    if age.isnumeric():
        ageNum = True
        print(F"Attempt:{counter}")
        print(f"You are {age} years old")
    elif counter == 5:
        print(f"You're out of luck")
        break

