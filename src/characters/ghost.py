from .monster import GameCharacter
from threading import Timer
from random import randint
from time import sleep


class Ghost(GameCharacter):

    def __init__(self, game, x, y, image, name):
        GameCharacter.__init__(self, game)
        self.y = y
        self.x = x
        self.dir = ''
        self.name = name
        self.image = image
        self.aux = 0
        self.game = game

    def move(self):
        self.aux = 0
        if self.game.ghostbreak == 0:
            while self.aux == 0:
                sleep(0.05)
                randir = randint(0, 4)

                if randir == 1 and self.dir != 'down' and self.y > 0:
                    self.dirtest('up')

                if randir == 2 and self.dir != 'up' and self.y < (len(self.game.matrix) - 1):
                    self.dirtest('down')

                if randir == 3 and self.dir != 'left' and self.x < (len(self.game.matrix[0]) - 1):
                    self.dirtest('right')

                if randir == 4 and self.dir != 'right' and self.x > 0:
                    self.dirtest('left')

    def nextlevelcoord(self, x, y):
        self.y = y
        self.x = x
        if self.game.level == 2:
            self.timeghost = 0.5
        if self.game.level == 3:
            self.game.timeghost = 0.3
        if self.game.level > 3:
            self.game.timeghost = self.game.timeghost / 2

    def ghostdisplay(self, new_x, new_y):
        self.game.canvas.delete("image{}".format(self.name))
        self.game.canvas.create_image(new_x * self.game.cellsize + self.game.cellsize / 2,
                                      new_y * self.game.cellsize + self.game.cellsize / 2,
                                      image=self.image, tags="image{}".format(self.name))

    def dirtest(self, direction):
        x, y = self.get_new_coord(direction)
        if 0 <= y < len(self.game.matrix) and 0 <= x < len(self.game.matrix[0]):
            if GameCharacter.can_move(x, y, self.game.matrix) == 1:
                self.ghostdisplay(x, y)
                self.x = x
                self.y = y

                self.aux = 1
                self.dir = direction
                if self.confrontation() == 1:
                    self.game.pacman.loselife()
                    if self.game.life == 0:
                        self.game.pacman.death()
                return Timer(self.game.timeghost, self.move).start()
        return 1
