from .monster import GameCharacter
from time import sleep


class Pacman(GameCharacter):

    def __init__(self, game):
        GameCharacter.__init__(self, game)
        self.x = 0
        self.y = 0
        self.mvtcount = 0
        self.refreshtime = 0.001
        self.changepac = 0.03

    def move(self, direction):
        if 0 <= self.x < self.game.width and 0 <= self.y < self.game.height:
            x, y = self.get_new_coord(direction)
            if 0 <= x < self.game.width and 0 <= y < self.game.height:
                if GameCharacter.can_move(x, y, self.game.matrix) == 1:
                    old_x = self.x
                    old_y = self.y
                    self.x = x
                    self.y = y
                    if self.game.matrix[self.y][self.x] == 2 or self.game.matrix[self.y][self.x] == 0:
                        self.ghostappear()
                        if 0 <= y < (len(self.game.matrix)) and 0 <= x < (len(self.game.matrix[0])):
                            if direction == 'up':
                                pm = self.game.image[1 + self.game.invicible * 2][0]
                                pmo = self.game.image[0 + self.game.invicible * 2][0]
                            if direction == 'down':
                                pm = self.game.image[1 + self.game.invicible * 2][1]
                                pmo = self.game.image[0 + self.game.invicible * 2][1]
                            if direction == 'right':
                                pm = self.game.image[1 + self.game.invicible * 2][3]
                                pmo = self.game.image[0 + self.game.invicible * 2][3]
                            if direction == 'left':
                                pm = self.game.image[1 + self.game.invicible * 2][2]
                                pmo = self.game.image[0 + self.game.invicible * 2][2]
                            self.pacamandisplay(old_x, old_y, pm, pmo)
                            if self.game.matrix[self.y][self.x] == 2:
                                self.pointadd()
                            self.clearleververif()
        if self.confrontation() == 1:
            self.loselife()
            if self.game.life == 0:
                self.death()

    def pacamandisplay(self, old_x, old_y, pm, pmo):
        self.game.canvas.delete('circ_{}{}'.format(old_x, old_y))
        self.game.canvas.delete("rectp")
        self.game.canvas.create_rectangle(old_x * self.game.cellsize, old_y * self.game.cellsize,
                                          (old_x + 1) * self.game.cellsize, (old_y + 1) * self.game.cellsize,
                                          fill='black', tags="rectp")

        self.game.canvas.create_image(self.x * self.game.cellsize + self.game.cellsize / 2,
                                      self.y * self.game.cellsize + self.game.cellsize / 2,
                                      image=pm, tags='imagep')
        #sleep(self.changepac)
        self.game.canvas.delete("imagep")
        sleep(self.refreshtime)
        self.game.canvas.create_image(self.x * self.game.cellsize + self.game.cellsize / 2,
                                      self.y * self.game.cellsize + self.game.cellsize / 2,
                                      image=pmo, tags='imagep')
        sleep(self.changepac)
        self.game.canvas.delete("imagep")
        sleep(self.refreshtime)
        self.game.canvas.create_image(self.x * self.game.cellsize + self.game.cellsize / 2,
                                      self.y * self.game.cellsize + self.game.cellsize / 2, image=pm, tags='imagep')
        sleep(self.changepac)
        self.game.canvas.delete("imagep")
        sleep(self.refreshtime)
        self.game.canvas.create_image(self.x * self.game.cellsize + self.game.cellsize / 2,
                                      self.y * self.game.cellsize + self.game.cellsize / 2,
                                      image=pmo, tags='imagep')
        sleep(self.changepac)

    def loselife(self):
        self.x = 0
        self.y = 0
        self.game.life = self.game.life - 1
        self.game.countlife.config(text="il vous reste {} vie".format(self.game.life))
        sleep(1)
        self.game.canvas.delete("rectp")
        self.game.canvas.create_rectangle(self.x * self.game.cellsize, self.y * self.game.cellsize,
                                          (self.x + 1) * self.game.cellsize,
                                          (self.y + 1) * self.game.cellsize, fill='black', tags="rectp")
        self.game.canvas.delete("imagep")
        self.game.canvas.create_image(self.game.cellsize / 2, self.game.cellsize / 2,
                                      image=self.game.image[0][3], tags="imagep")

    def death(self):
        self.game.ghostbreak = 0
        self.game.ghostbreaker()
        self.game.victoryevent.config(text='defeat !!!!')
        self.game.defeatevent()

    def clearleververif(self):
        if self.game.matrix == self.game.check:
            self.game.victoryevent.config(text="next level")
            self.game.ghostbreak = 0
            self.mvtcount = 0
            self.game.ghostbreaker()
            sleep(4)
            self.game.victoryevent.config(text="")
            self.game.changelevel()

    def pointadd(self):
        self.game.point += self.game.multiplicator
        self.game.point = int(self.game.point)
        self.game.countpoint.config(text=self.game.point)
        self.game.matrix[self.y][self.x] = 0

    def ghostappear(self):
        n = len(self.game.tableghost)
        self.mvtcount += 1
        reste = self.mvtcount % 2
        quotient = (self.mvtcount // 2) - 1
        if reste == 0 and quotient <= n - 1:
            self.game.tableghost[quotient].move()
