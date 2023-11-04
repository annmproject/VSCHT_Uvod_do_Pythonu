from abstract_classes import AbstractDungeon
from copy import deepcopy
from map_entities import Hero, Goblin
import random

# magic constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Dungeon(AbstractDungeon):
    def __init__(self, size: tuple, tunnel_number: int, hero_name: str):
        super().__init__(size)
        self.hero = Hero("@", hero_name, [1, 1], 5, 5, 1)
        self.tunnel_number = tunnel_number
        self.starting_entities = ["goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin",
                                  "goblin", "goblin", "goblin", "goblin"]
        self.entities = []
        self.empty_space = []
        self.message = ""
        self.create_dungeon()

    def __str__(self):
        printable_map = ""
        for row in self.current_map:
            for column in row:
                printable_map += column
            printable_map += "\n"
        return printable_map

    def create_dungeon(self):
        # init full map
        self.dungeon_map = [['▓' for _ in range(self.size[1])] for _ in range(self.size[0])]
        # position (1,1) must be empty
        self.dungeon_map[1][1] = '.'
        # fields in map
        no_fields = (self.size[0] - 2) * (self.size[1] - 2)
        # generate path from first positions until empty field is not at least 70 pct
        curr_pos = (1, 1)
        while int((sum(row.count('.') for row in self.dungeon_map) / no_fields) * 100) < 70:
            # generate direction
            direction = random.randint(0, 3)
            # calculate max path length
            max_path_length = 0
            if direction == UP:
                max_path_length = abs(1 - curr_pos[0])
            elif direction == DOWN:
                max_path_length = abs(self.size[0] - 2 - curr_pos[0])
            elif direction == LEFT:
                max_path_length = abs(1 - curr_pos[1])
            elif direction == RIGHT:
                max_path_length = abs(self.size[1] - 2 - curr_pos[1])
            # generate path length
            path_length = random.randint(0, max_path_length)
            # write path in direction
            for _ in range(path_length):
                if direction == UP:
                    curr_pos = (curr_pos[0] - 1, curr_pos[1])
                elif direction == DOWN:
                    curr_pos = (curr_pos[0] + 1, curr_pos[1])
                elif direction == LEFT:
                    curr_pos = (curr_pos[0], curr_pos[1] - 1)
                elif direction == RIGHT:
                    curr_pos = (curr_pos[0], curr_pos[1] + 1)
                self.dungeon_map[curr_pos[0]][curr_pos[1]] = '.'
                if (curr_pos[0], curr_pos[1]) != (1, 1):
                    self.empty_space.append(curr_pos)
        # place entities
        self.place_entities(self.starting_entities)
        # deepcopy of dungeon map
        self.current_map = deepcopy(self.dungeon_map)
        # unique list of empty spaces
        self.empty_space = list(map(list, set(self.empty_space)))
        # write hero into map
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier

    def hero_action(self, action):
        if action == "R":
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1] + 1] != "▓":
                self.hero.position[1] += 1
        elif action == "L":
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1] - 1] != "▓":
                self.hero.position[1] -= 1
        elif action == "U":
            if self.dungeon_map[self.hero.position[0] - 1][self.hero.position[1]] != "▓":
                self.hero.position[0] -= 1
        elif action == "D":
            if self.dungeon_map[self.hero.position[0] + 1][self.hero.position[1]] != "▓":
                self.hero.position[0] += 1
        elif action == "A":
            fighting = False
            for entity in self.entities:
                if tuple(self.hero.position) == entity.position:
                    if hasattr(entity, "attack"):
                        self.fight(entity)
                        fighting = True
            if not fighting:
                self.message = "Your big sword is hitting air really hard!"

        self.update_map(self.entities)

        if self.hero.hp < 1:
            self.message += "\nTHIS IS THE END"

    def place_entities(self, entities: list):
        print(self.empty_space)
        position = random.sample(self.empty_space, len(entities))
        for idx, entity in enumerate(self.starting_entities):
            if entity == "goblin":
                self.entities.append(Goblin(identifier="\033[38;5;1mg\033[0;0m",
                                            position=position[idx], base_attack=-1,
                                            base_ac=0, damage=1))
        for entity in self.entities:
            self.dungeon_map[entity.position[0]][entity.position[1]] = entity.map_identifier

    def update_map(self, entities: list):
        # TODO implement entities
        self.current_map = deepcopy(self.dungeon_map)
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier

    def fight(self, monster):
        hero_roll = self.hero.attack()
        monster_roll = monster.attack()
        if hero_roll["attack_roll"] > monster.base_ac:
            monster.hp -= hero_roll["inflicted_damage"]
            if monster.hp > 0:
                self.message = f"Hero inflicted {hero_roll['inflicted_damage']}"
            else:
                self.message = f"Hero Hero inflicted {hero_roll['inflicted_damage']} damage and slain {monster}"
                self.hero.gold += monster.gold
                self.hero.xp += 1
                self.dungeon_map[monster.position[0]][monster.position[1]] = "."
                self.entities.remove(monster)
        if monster_roll["attack_roll"] > self.hero.base_ac:
            self.message += f"\nMonster inflicted {monster_roll['inflicted_damage']} damage"
            self.hero.hp -= monster_roll['inflicted_damage']
            if self.hero.hp < 1:
                self.message += f"{self.hero.name} have been slained by {monster}"
        self.message += f"\nHero HP: {self.hero.hp}  Monster HP: {monster.hp}"
