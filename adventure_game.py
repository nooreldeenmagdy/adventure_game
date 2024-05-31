# Run the game by entering python3 adventure_game.py in the terminal

import time
import random
sleep_time = 2


def print_pause(text):
    # Prints the events of game in a custom speed.
    
    global sleep_time
    fun_sleep = sleep_time
    print(text)
    time.sleep(fun_sleep)
    
def check_score_turns(total_score, no_turns):
    # Checks if the score or the number of the turns reaches zero.
    
    if (total_score <= 0) or (no_turns <= 0):
        print_pause("You have been defeated!, GAME OVER")
        play_again()

    
def intro(option, total_score, no_turns):
    # Prints the introduction of the game.
    
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) magic wand.")
    print_pause("You have a total score of " + str(total_score) + " points. The score is changed according to your choices in the game world.")
    print_pause("You have a total of " + str(no_turns) + " turns to win the game.")
    print_pause("The game is over if you are attacked by the " + option + " and wins or your (score or turns) reachs ZERO.")
    
    


def field(item, option, total_score, no_turns):
    # Things that happen when the player runs back to the field.
    
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    
    while True:
        player_input_1 = input("(Please enter 1 or 2).")
        if player_input_1 == "1":
            house(item, option, total_score, no_turns)
            break
        elif player_input_1 == "2":
            cave(item, option, total_score, no_turns)
            break

def house(item, option, total_score, no_turns):
    # Things that happen to the player in the house.
    
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " + option + ".")
    print_pause("Eep! This is the " + option + "'s house!")
    print_pause("The " + option + " attacks you!")
    no_turns -= 1
    print_pause("You have consumed 1 turn and you have " + str(no_turns) +" left.")
    check_score_turns(total_score, no_turns)
    
    defend(item, option, total_score, no_turns)
            

def cave(item, option, total_score, no_turns):
    # Things that happen to the player goes in the cave. 

    if "Ogoroth" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        total_score -= 5
        print_pause("You have a total score of " + str(total_score) + " points. ")
        no_turns -= 1
        print_pause("You have consumed 1 turn and you have " + str(no_turns) +" left.")
        check_score_turns(total_score, no_turns) 
        print_pause("You walk back to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical wand of Ogoroth!")
        total_score += 5
        print_pause("You have a total score of " + str(total_score) + " points.")
        no_turns -= 1
        print_pause("You have consumed 1 turn and you have " + str(no_turns) +" left.")
        check_score_turns(total_score, no_turns) 
        print_pause("You discard your silly old wand and take the wand of Ogoroth with you.")
        print_pause("You walk back out to the field.")
        item.append("Ogoroth")
        
    field(item, option, total_score, no_turns)
    
    
def defend(item, option, total_score, no_turns):
    # Things that happen when the player is approached by an enemy.  

    if "Ogoroth" not in item:
        print_pause("You feel a bit under-prepared for this, what with only having a tiny magic wand.")
    while True:
        player_input_2 = input("Would you like to (1) fight or (2) run away?")
        if player_input_2 == "1":
            if "Ogoroth" in item:
                print_pause("As the " + option + " moves to attack, you unsheath your new wand.")
                print_pause("The wand of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
                print_pause("But the " + option + " takes one look at your shiny new toy and runs away!")
                total_score += 10
                print_pause("You have a total score of " + str(total_score) + " points.")
                no_turns -= 1
                print_pause("You have consumed 1 turn and you have " + str(no_turns) +" left.")
                print_pause("You have rid the town of the " + option + ". You are victorious!")
            else:
                print_pause("You do your best...")
                print_pause("but your wand is no match for the " + option + ".")
                total_score = 0
                print_pause("You have a total score of " + str(total_score) + " points.")
                print_pause("You have been defeated!, GAME OVER")
            play_again()
            break
            
        if player_input_2 == "2":
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
            total_score -= 5
            print_pause("You have a total score of " + str(total_score) + " points. ")
            no_turns -= 1
            print_pause("You have consumed 1 turn and you have " + str(no_turns) +" left.")
            check_score_turns(total_score, no_turns)  
            field(item, option, total_score, no_turns)
            break


def play_again():
    # Gives the option to play the game again or not.
    
    player_input_3 = input("Would you like to play again? (y/n)").lower()
    if player_input_3 == "y":
        print_pause("Great! Restarting the game.")
        play_game()
    elif player_input_3 == "n":
        print_pause("Thank you for playing the adventure game!")
    else:
        play_again()

#########################

def play_game():
    # Starts the game.
 
    item = []
    total_score = 10 # Initial score for the player.
    no_turns = 3 # Initial number of turns for the player.
    option = random.choice(["Wicked Fairy", "Pirate", "Dragon", "gorgon"])
    
    intro(option, total_score, no_turns)
    field(item, option, total_score, no_turns)


play_game()
