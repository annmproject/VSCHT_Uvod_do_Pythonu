import random

# magic constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Dungeon:

    def __init__(self, size: tuple[int, int]):
        """ Constructor initializes default map. """
        self.size = size
        self.map = [['▓' for _ in range(size[1])] for _ in range(size[0])]
        self.map[1][1] = '.'

    def print_map(self):
        """ The method prints map. """
        for row in self.map:
            print(''.join(row))

    def print_nice_map(self):
        """ The method prints map in nice way. """
        for row in self.map:
            print(' '.join(row))

    def get_percentage_of_dot_fields(self) -> int:
        """ The method returns percentage of dot fields. """
        no_fields = (self.size[0] - 2) * (self.size[1] - 2)
        no_dot_fields = sum(row.count('.') for row in self.map)
        return int((no_dot_fields / no_fields) * 100)

    def generate_paths(self, bound: int) -> None:
        """ The method generates paths until we make [bound] % of board with dot. """
        curr_pos = (1, 1)
        while self.get_percentage_of_dot_fields() < bound:
            direction = random.randint(0, 3)
            max_path_length = 0
            if direction == UP:
                max_path_length = abs(1 - curr_pos[0])
            elif direction == DOWN:
                max_path_length = abs(self.size[0] - 2 - curr_pos[0])
            elif direction == LEFT:
                max_path_length = abs(1 - curr_pos[1])
            elif direction == RIGHT:
                max_path_length = abs(self.size[1] - 2 - curr_pos[1])
            path_length = random.randint(0, max_path_length)
            curr_pos = self.build_path(curr_pos, direction, path_length)

    def build_path(self, curr_pos: tuple[int, int], direction: int, length: int) -> tuple[int, int]:
        """ The method builds dot path and return end position. """
        for _ in range(length):
            if direction == UP:
                curr_pos = (curr_pos[0] - 1, curr_pos[1])
            elif direction == DOWN:
                curr_pos = (curr_pos[0] + 1, curr_pos[1])
            elif direction == LEFT:
                curr_pos = (curr_pos[0], curr_pos[1] - 1)
            elif direction == RIGHT:
                curr_pos = (curr_pos[0], curr_pos[1] + 1)
            self.map[curr_pos[0]][curr_pos[1]] = '.'
        return curr_pos


if __name__ == "__main__":
    dungeon = Dungeon((14, 38))
    dungeon.generate_paths(40)
    # dungeon.print_nice_map()
    dungeon.print_map()
