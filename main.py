print("Welcome to my first game\n")
name = input("What is your name?\n")
age = int(input("What is your age?\n"))

health = 30

if age >= 18:
    print("Yay! ", "You are old enough!", "\n")

    wants_to_play = input("Do you want to join me on a Magick Quest? \n").lower()
    if wants_to_play == "yes":
        print("Excellent!")
        print("You are starting with", health, "health", "\n")
        print("Let the magick begin!!!!", "\n")
        print("This is a quest to recover a magickal sword named 'Stormbringer'.\n"
              "'Stormbringer' is able to grant the soul energy of those who are slain to the slayer who wields the"
              "sword.\n"
              "'Stormbringer' belonged to an ancient King and was thought to be lost deep in the forest of "
              "Ultmulga.\n"
              "He/She/They that possesses 'Stormbringer' will inherit the Kingdom of the ancient King.\n"
              "Your first choice is critical...choose wisely. \n")
        print("The left path is dark and full of shadows...definitely hard to see and an eerie sound is emitting\n"
              "from further down the path.\n")
        print("To the right is a brightly lit path with birds a flutter and the sun is "
              "shining.", "\n")
        left_or_right = input("Do you want to go down the left or right path?(left/right)? \n").lower()

        if left_or_right == "left":
            print("Excellent Traveler! You are a brave one. You may just be the one to find 'Stormbringer'")
            ans = input("You take the dark path and come to a lake dark as night...do you swim across or attempt to "
                        "go around (across/around)? \n").lower()
            if ans == "around":
                print("You went around and reached the other side of the lake unscathed but the forest fairies laugh "
                      "at your cowardice.", "\n")
                health -= 3
                print("You lose 3 health.")
                print("Health = 27", "\n")
            elif ans == "across":
                print("You swim across the murky darkness only to get attacked by a Megalodon midway.\n"
                      "You survive but at a cost.\n"
                      "You lose 5 health.")
                health -= 5
                if health >= 27:
                    print("Health = 22", "\n")
                else:
                    print("Health = 25", "\n")
            print("After a fire to warm up, you notice a wicked looking house further up the hill.\n"
                  "But you also notice the river is teeming with fish and you are starving.\n")
            ans = input("Which do you choose...Traveler...your belly or the unknown of the house"
                        "(river/house)?\n").lower()
            if ans == "house":
                print("You enter the house and immediately start choking from a dark magick spell.\n")
                print("You lose 5 health.")
                health -= 5
                if health == 22:
                    print("Health = 17", "\n")
                else:
                    print("Health = 20", "\n")
                    print("You have survived unceremoniously and may continue.\n")
                    print("You leave the house and see a forest behind it so you enter.\n"
                          "In the forest you find a grave that looks very very old and like it has not been "
                          "touched in ages.\n")
                ans = input("Do you dig up the grave or venture further into the forest (dig/venture)? \n").lower()
                if ans == "dig":
                    print("You are a truly valiant and worthy soul. You find the body of the ancient King.\n"
                          "You take 'Stormbringer' from his cold dead fingers and feel a surge of power\n")
                    print("Congratulations!!! You have won the game and now own the Ancient Kingdom!!!")
                else:
                    print("You fool!!! You have passed up glory!!\n"
                          "The ghost of the Ancient King rises from the grave and kills you!\n")
                    print("GAME OVER")
            else:
                print("As you attempt to assuage your hunger you fall into the river\n"
                      "that has now become lava and you lose, mortal!!!")
        else:
            print("Tsk.Tsk.Tsk...this book's cover is not what it seems. You are attacked by death and lose all of "
                  "your health...GAME OVER")

    else:
        print("too bad...but may you be enchanted")

else:
    print("Sorry, but you're not old enough to play this game...")
