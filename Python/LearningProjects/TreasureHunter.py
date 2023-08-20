import random
import time
gem=['Azuirite','Banded Agate', 'Blue Quartz', 'Eye Agate','Hematite','Lapis Lazuli', 'Malachite', 'Moss Agate','Obsidian','Rhodochrosite',"Tiger's Eye", 'Turquoise']
metal = ['Iron', 'Silver', 'Gold', 'Platinum','Mithril']
type = ['Necklace', 'Bracelet', 'Ring', 'Pendant', 'Ear ring']
enchant = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
treasure = metal[random.randrange(len(metal)-1)]+" "+ type[random.randrange(len(type)-1)]+" set with "+ gem[random.randrange(len(gem)-1)]+" of "+enchant[random.randrange(len(enchant)-1)]+" +"+str((random.randrange(5)+1))

def you_died():
    print('You died in the most horrible way possible.')
    play_again()

def you_won():
    print(f"you found a {treasure}!")
    time.sleep(.5)
    print ("but")
    time.sleep(.5)
    you_died()


def play_again():
    choice = input("Would you like to try again? y/n\n")
    if (choice.lower() == "y"):
        playgame()
    else:
        print("Thanks for trying my game!")
        exit()


def playgame():
    print('You hear rumors of a treasure hidden in this forest, you begin your search on a path\nBeware, there area evils in this forest')
    #first choice left or right
    choice = input('\nyou find yourself at a fork in the path do you go left or right? [left | right]\n')
    if (choice.lower() != "left"):
        you_died()

    #second choice wait or swim
    choice = input('\nyou see an island in the middle of a lake swim across or wait for a boat? [swim | wait]\n')
    if (choice.lower() != "wait"):
        you_died()
    
    #third choice Red Yellow or Blue
    choice = input('\nyou come up to a hut with three doors, which do you choose? [Red | Yellow | Blue]\n')
    if (choice.lower() == "red"):
        you_died()
    if (choice.lower() == "blue"):
        you_died()
    if (choice.lower() == "yellow"):
        you_won()

playgame()



