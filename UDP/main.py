from dungeon import Dungeon
import subprocess

if __name__ == "__main__":
    hero_name = input("What is your name hero?")
    dungeon = Dungeon(size=(10, 10), tunnel_number=40, hero_name=hero_name)
    while True:
        subprocess.Popen("cls", shell=True).communicate()
        print(dungeon)
        print(dungeon.message)
        action = input(f"Select an action {hero_name}: (L)EFT, (R)IGHT, (D)OWN, (U)P, (A)TTACK, (Q)UIT")
        if action == "Q":
            print("You coward!")
            exit(0)
        else:
            dungeon.hero_action(action)
        if dungeon.hero.hp < 1:
            print(dungeon.message)
            exit(0)