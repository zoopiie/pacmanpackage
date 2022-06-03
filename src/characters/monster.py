class GameCharacter:
    def __init__(self, game):
        self.game = game
    def get_new_coord(self, dir):
        if dir == 'up':
            y = self.y - 1
            x = self.x
        elif dir == 'down':
            y = self.y + 1
            x = self.x
        elif dir == 'left':
            y = self.y
            x = self.x - 1
        elif dir == 'right':
            y = self.y
            x = self.x + 1
        else:
            x = self.x
            y = self.y
        return x, y

    def can_move(new_x, new_y, matrix):
        if matrix[new_y][new_x] == 0 or matrix[new_y][new_x] == 2:
            return 1
        return 0

    can_move = staticmethod(can_move)

    def confrontation(self):
        if self.game.invicible == 0:
            for i in range(len(self.game.tableghost)):
                if self.game.pacman.x == self.game.tableghost[i].x and self.game.pacman.y == self.game.tableghost[i].y:
                    return 1
        return 0

