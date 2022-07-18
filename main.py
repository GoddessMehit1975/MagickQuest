print("Welcome to my first game")
name = input("What is your name?")
age = int(input("What is your age?"))

health = 15

if age >= 18:
    print("You are old enough!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play!!!!")
        left_or_right = input("First choice... left or right(left/right)? ")
        if left_or_right == "left":

            ans = input(
                "Nice, you follow the path and you reach lake...Do you want to swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")

            elif ans == "across":
                print("You managed to get across, but were bitten by a pirahna and lost 5 health.")
                health -= 5
                print("Health = 10")

            ans = input("You notice a house and a river.  Which do you go to (river/house)? ")
            if ans == "house":
                print("You enter the house and lose 5 health due to a magick spell.")
                health -= 5
                print("Health = 5")
                if health <= 0:
                    print("You now have 0 health and lose the game")
                else:
                    print("You have survived and may continue.")

            else:
                print("You fell in the river and lost...")

        else:
            print("You lost...")

    else:
        print("Live long and prosper")

else:
    print("Sorry, but you're not old enough to play this game...")

