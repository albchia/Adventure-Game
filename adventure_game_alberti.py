import time
import random


def print_pause(message_to_print, seconds=0.2):
    print(message_to_print)
    time.sleep(seconds)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            break
        elif option2 in choice:
            break
        else:
            print(choice)
    return choice


def intro(weapon, creature):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature +
                " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def cave(weapon, creature):
    if "sword" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You have been here before "
                    "and gotten all the good stuff.")
        print_pause("It's just an empty cave now.")
        print_pause("You walk back to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        weapon.append("sword")
    choose_game(weapon, creature)


def house(weapon, creature):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + creature + ".")
    print_pause("Eep! This is the " + creature + "'s house!")
    print_pause("The " + creature + " attacks you!")

    if "sword" not in weapon:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        run_fight(weapon, creature)

    run_fight(weapon, creature)


def run_fight(weapon, creature):
    choice_1_2 = valid_input("Would you like to (1) fight "
                             "or (2) run away?", "1", "2")

    if choice_1_2 == "1":
        if "sword" in weapon:
            print_pause("As the " + creature + " moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand "
                        "as you brace wyourself for the attack.")
            print_pause("The " + creature +
                        " takes one look at your shiny "
                        "new weapon and runs away!")
            print_pause("You are victorious!\n")
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match "
                        "for the " + creature + ".")
            print_pause("You have been defeated!")
        play_again()

    elif choice_1_2 == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        choose_game(weapon, creature)


def choose_game(weapon, creature):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    choice_1_2 = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if choice_1_2 == "1":
        house(weapon, creature)
    elif choice_1_2 == "2":
        cave(weapon, creature)


def play_again():
    choice_y_n = valid_input("Would you like to play again? (y/n)",
                             "y", "n")
    if choice_y_n == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif choice_y_n == "n":
        print_pause("Thanks for playing! "
                    "See you next time.")
    else:
        play_again()


def play_game():
    weapon = []
    creature = random.choice(["dragon", "pirate", "troll",
                              "wicked fairie", "gorgon", "clown"])
    intro(weapon, creature)
    choose_game(weapon, creature)


if __name__ == '__main__':
    play_game()
