from dungeon import Dungeon
from datetime import datetime
import pickle
import os


if __name__ == "__main__":

    hero_name = None
    dungeon = None

    while True:

        # ask for action
        action = input(f"Select an action: (N)ew game, (L)oad game: ")

        # new game
        if action == 'N':

            # get hero name
            hero_name = input("What is your name hero? ")

            # check name
            if not (hero_name.isalpha() and hero_name.isascii()):
                print("Invalid name")
                continue

            # create dungeon
            dungeon = Dungeon(size=(10, 10), tunnel_number=40, hero_name=hero_name)

            # break cycle
            break

        # load game
        elif action == 'L':

            while True:

                # get path
                path = input(f"path to the saved game: ")

                # path does not exist
                if not os.path.exists(path):
                    print("Path does not exists!")
                    continue

                # file is not DNG
                if not path.lower().endswith('.dng'):
                    print("Expected .dng file!")
                    continue

                # load saved game
                try:
                    with open(path, "rb") as file:
                        hero_name, dungeon = pickle.load(file)
                        break
                except:
                    print("Damaged file!")
                    continue

            # break infinite cycle
            break

    # play game
    while True:

        # multiplatform clear
        os.system('cls' if os.name == 'nt' else 'clear')

        print(dungeon)
        print(dungeon.message)
        action = input(f"Select an action {hero_name}: (L)EFT, (R)IGHT, (D)OWN, (U)P, (A)TTACK, (Q)UIT: ")

        # end game
        if action == "Q":

            while True:

                # save or not
                action = input(f"Do you, {hero_name}, want to save a game?: (Y)es or (N)o? ")

                # invalid input
                if not (action == 'N' or action == 'Y'):
                    continue

                # yes -> serialize object
                if action == 'Y':
                    filename = hero_name + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.dng'
                    with open(filename, "wb") as file:
                        pickle.dump((hero_name, dungeon), file)
                    print("Game saved to", filename)

                print("Bye!")
                exit(0)

        else:
            dungeon.hero_action(action)
        if dungeon.hero.hp < 1:
            print(dungeon.message)
            exit(0)
