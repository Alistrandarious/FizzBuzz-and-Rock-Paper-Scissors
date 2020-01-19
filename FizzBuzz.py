import time
number = 0
counter = 0
bonusMode = False
ageNum = False
loopout = False

print("Welcome to Fizz/Buzz!")
name = input("What's your name, stranger?\n").capitalize()

while name != "David":
    print("Ah, yes... I know your barber. " + name + "; welcome!\n")
    break
while name == "Oli":
    time.sleep(3)
    print("Oh for fu-.")
    exit()
while name.isnumeric():
    print("Ah, a fellow computer. Beep boop!\n")
    break
while name == "David":
    print("Ah! David Harvey the socialist geographer! Welcome!\n")
    break


while not ageNum:

    age = input("How old are you?\n")
    while not age.isnumeric() and loopout is False:
        print("Why you trying to break my code? I'm deleting your system 32.")
        print("...")
        time.sleep(1)
        print("Oh wait, this is my laptop.\n")
        ageNum = False
        loopout = True
        time.sleep(0.5)
        age = input("PLEASE ENTER A NUMBER: how old are you?\n")
        counter += 1
    while not age.isnumeric():
        input("please just... Enter a number.\n")
        counter += 1
        if loopout is True and counter >= 5:
            print("How persistent... Please come back when you are less annoying.")
            exit()
    if int(age) >= 18 and int(age) % 15 == 0:
        print(f"BONUS MODE: YOUR AGE IS DIVISIBLE BY BOTH 3 and 5 AND EVERYTHING IS NOW IN"
              "CAPS!!!!!11!!1one!!!")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("...")
        time.sleep(0.3)
        print("\nPlayer information accepted...\n Beginning FizzBuzz.\n")
        ageNum = True
        bonusMode = True
        break
    elif int(age) >= 18:
        ageNum = True
        print(f"Player information accepted...\n Beginning FizzBuzz.\n")
        break
    elif int(age) == 17:
        print("Sorry! You're too young. Come back next year.\n")
        exit()
    elif int(age) < 17:
        print(f"Sorry, you are too young! Try again in " + str(18 - int(age)) + " years.\n")
        ageNum = False
        exit()
    elif counter == 5:
        print(f"Tries to type in numbers expired. Please check yourself before you wreck yourself.\n\n\n")
        exit()
    else:
        exit()
while ageNum is True and bonusMode is False:
    print("Running Fizz/Buzz in 3")
    time.sleep(1)
    print("Running Fizz/Buzz in 2")
    time.sleep(1)
    print("Running Fizz/Buzz in 1\n\n\n")
    time.sleep(1)
    break

while ageNum is True and bonusMode is True:
    print("RUNNING THA BONUS MODE FIZZ BUZZ IN 3")
    time.sleep(1)
    print("IN 2 OH MY GOD 2")
    time.sleep(1)
    print("111111111111111111111111\n\n\n")
    time.sleep(1)
    break
if bonusMode is False:
    print("Go!\n")
if bonusMode is True:
    print("LETS GOOOOOOOOOOOOOOO!!!!!!!!\n")

while number <= 149:
    number += 1
    time.sleep(0.15)
    if ((number % 3 == 0) and (number % 5 == 0)) and bonusMode is False:
        print("Fizz Buzz")
    if bonusMode is True and (number % 3 == 0) and (number % 5 == 0):
        print("FIZZ BUZZ!!!! YEAHHHHH!!!!!")
    elif number % 3 == 0 and bonusMode is False:
        print("Fizz")
    elif bonusMode is True and (number % 3 == 0):
        print("FIZZZZZ!!!!!!")
    elif number % 5 == 0 and bonusMode is False:
        print("Buzz")
    elif bonusMode is True and (number % 5 == 0):
        print("BUZZ!!!!!!!!!!")
    else:
        print(str(number))

print("Thanks for playing Fizz/Buzz.")
restart = input("Would you like to play again?\n").capitalize()
if restart in "Y" and bonusMode is False:
    print("Purchase DLC from David Harvey for £5.99")
if restart in "Y" and bonusMode is True:
    print("PURCHASE DLC FROM DAVID HARVEY FOR £5.99")
if restart in "N" and bonusMode is False:
    print("What, not good enough for ya? Get outta here Sprandiik!")
    exit()
if restart in "N" and bonusMode is True:
    print("WHAT, NOT GOOD ENOUGH FOR YA EVEN WITH BONUS MODE? GET OUTTA HERE AND BACK TO NEW FOLKINGHAM, SPRANDIIK!")
    exit()
else:
    print("IT WAS A YES OR NO QUESTION! (ノಠ益ಠ)ノ彡┻━┻")

print(r"""\

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /

                  brought to you by Llama studios
                            est. 1995
                """)






