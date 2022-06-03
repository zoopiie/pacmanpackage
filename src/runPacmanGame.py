import Level
import copy
from characters.pacman import Pacman
import characters.ghost
import controls
from tkinter import *


class Game:

    def __init__(self, levelnumber):
        self.width = len(levelnumber[0])
        self.height = len(levelnumber)
        self.matrix = copy.deepcopy(levelnumber)
        self.check = copy.deepcopy(levelnumber)
        self.level = 1
        self.point = 0
        self.life = 3
        self.multiplicator = 1
        self.tableghost = []
        self.ghostbreak = 0
        self.timeghost = 1
        self.cheatingvar = 0
        self.anticheatvar = 0
        self.invicible = 0
        self.pacman = None
        self.victoryevent = None
        self.countpoint = None
        self.countlevel = None
        self.countlife = None
        self.canvas = Canvas(root, width=0, height=0, bg='black')
        self.cellsize = 55
        self.cir = 10
        self.image = []

    def matrix_setup(self):
        if self.level == 2:
            self.width = len(Level.leveltwo[0])
            self.height = len(Level.leveltwo)
            self.matrix = copy.deepcopy(Level.leveltwo)
            self.check = copy.deepcopy(Level.leveltwo)
        if self.level >= 3:
            self.width = len(Level.levelthree[0])
            self.height = len(Level.levelthree)
            self.matrix = copy.deepcopy(Level.levelthree)
            self.check = copy.deepcopy(Level.levelthree)

    def create_circle(x, y, r, canvasname, i, j):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvasname.create_oval(x0, y0, x1, y1, fill='yellow', tags='circ_{}{}'.format(i, j))

    create_circle = staticmethod(create_circle)

    def defeatevent(self):
        canvas.delete('all')
        root.geometry('0x0')
        canvas.config(width=0, height=0)
        rt = Toplevel()
        rt.config(bg='black')
        Label(rt, text=" ton score est de : {}".format(self.point), fg='#00eeee', bg='black', font=('', 40, 'bold'))\
            .pack()
        if self.cheatingvar != 0:
            Label(rt, text='je sais que tu as triché....', fg='#00eeee', bg='black', font=('', 20, 'bold')).pack()

    def create(self):
        self.matrix_setup()
        self.canvas.delete("all")
        self.multiplicator = ((self.level / 10) + 1) * 10
        self.canvas.config(width=len(self.matrix[0]) * self.cellsize, height=len(self.matrix) * self.cellsize)
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 1:
                    self.canvas.create_rectangle(i * self.cellsize, j * self.cellsize, (i + 1) * self.cellsize,
                                                 (j + 1) * self.cellsize, fill='#002eee')
                if self.matrix[j][i] == 0:
                    self.canvas.create_rectangle(i * self.cellsize, j * self.cellsize, (i + 1) * self.cellsize,
                                                 (j + 1) * self.cellsize, fill='black')
                    self.create_circle((i * self.cellsize + self.cellsize / 2), (j * self.cellsize + self.cellsize / 2),
                                       self.cir, self.canvas, i, j)
        if self.cheatingvar != 0:
            self.canvas.create_image(self.cellsize / 2, self.cellsize / 2, image=game.image[2][3], tags='imagep')
        else:
            self.canvas.create_image(self.cellsize / 2, self.cellsize / 2, image=game.image[0][3], tags='imagep')
        self.matrixzerototwo()

    def matrixzerototwo(self):
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 0:
                    self.matrix[j][i] = 2
        self.matrix[0][0] = 0

    def changelevel(self):
        self.ghostbreak = 0
        self.level += 1
        self.setzeropacman()
        if self.anticheatvar == 0:
            if self.level == 2:
                self.countlevel.config(text="level {}".format(self.level))
                self.create()
            if self.level == 3:
                self.countlevel.config(text="level {}".format(self.level))
                self.create()
            if self.level > 3:
                if self.timeghost <= 0.2:
                    self.timeghost = self.timeghost / 2
                else:
                    self.timeghost = self.timeghost - 0.1
                self.countlevel.config(text="level {}".format(self.level))
                self.create()
            self.setzeroghost()
        else:
            self.defeatevent()

    def canvas_config(self):
        self.canvas.config(width=len(self.matrix[0]) * self.cellsize, height=len(self.matrix) * self.cellsize)

    def ghostbreaker(self):
        self.ghostbreak = 1 - self.ghostbreak
        if self.ghostbreak == 0:
            for i in range(len(self.tableghost)):
                self.tableghost[i].move()
        return self.ghostbreak

    def inviciblemode(self):
        self.invicible = 1 - self.invicible
        self.cheatingvar += 1
        self.anticheatvar = 1

    def tricheplus(self):
        self.anticheatvar = 0

    def discret(self):
        self.cheatingvar = 0

    def morelife(self):
        self.life += 1
        self.cheatingvar += 1
        self.anticheatvar = 1
        self.countlife.config(text="il te reste {} vie".format(self.life))

    def pointadd(self):
        self.point += 1563
        self.countpoint.config(text=self.point)

    def createghost(self, image, game, name):
        mynewghost = characters.ghost.Ghost(game, len(self.matrix[0]) - 1, len(self.matrix) - 1, image, name)
        return mynewghost

    def setzeroghost(self):
        for i in range(0, len(self.tableghost)):
            self.tableghost[i].x = len(self.matrix[0]) - 1
            self.tableghost[i].y = len(self.matrix) - 1

    def setzeropacman(self):
        self.pacman.x = 0
        self.pacman.y = 0


root = Tk()
root.title('pacman')
root.config(bg='black')


basePath = "C:/Users/Forgeur/Desktop/pacmanpackage/src/assets/"

matrixAssets = [[PhotoImage(file="{}pacmanopenhaut.png".format(basePath)),
                 PhotoImage(file="{}pacmanopenbas.png".format(basePath)),
                 PhotoImage(file="{}pacmanopengauche.png".format(basePath)),
                 PhotoImage(file="{}pacmanopendroite.png".format(basePath))],
                [PhotoImage(file="{}pacmanhaut.png".format(basePath)),
                 PhotoImage(file="{}pacmanbas.png".format(basePath)),
                 PhotoImage(file="{}pacmangauche.png".format(basePath)),
                 PhotoImage(file="{}pacmandroite.png".format(basePath))],
                [PhotoImage(file="{}chomphaut.png".format(basePath)),
                 PhotoImage(file="{}chompbas.png".format(basePath)),
                 PhotoImage(file="{}chompgauche.png".format(basePath)),
                 PhotoImage(file="{}chompdroite.png".format(basePath))],
                [PhotoImage(file="{}greycircle.png".format(basePath)),
                 PhotoImage(file="{}greycircle.png".format(basePath)),
                 PhotoImage(file="{}greycircle.png".format(basePath)),
                 PhotoImage(file="{}greycircle.png".format(basePath))],
                [PhotoImage(file="{}blinky2.png".format(basePath)),
                 PhotoImage(file="{}inky2.png".format(basePath)),
                 PhotoImage(file="{}pinky2.png".format(basePath)),
                 PhotoImage(file="{}clyde2.png".format(basePath))]
                ]


game = Game(Level.levelone)
controls.bind_controls(game)
game.image = matrixAssets


countlevel = Label(root, text="level {}".format(game.level), bg='black', fg='#00eeee', font=30)
countlevel.pack(side=LEFT, anchor=NW)
countpoint = Label(root, text="score : {}".format(game.point), bg='black', fg='#00eeee', font=30)
countpoint.pack(side=TOP, anchor=N)
victoryevent = Label(root, text="", bg='black', fg='#00eeee', font=30)
victoryevent.pack(side=RIGHT, anchor=NW)
countlife = Label(root, text="il te reste {} vie".format(game.life), bg='black', fg='#00eeee', font=30)
countlife.pack(side=LEFT, anchor=NW)

canvas = Canvas(root, width=0, height=0, bg='black')
canvas.pack(side=LEFT)

game.countlevel = countlevel
game.countpoint = countpoint
game.countlife = countlife
game.victoryevent = victoryevent
game.canvas = canvas

blinky = game.createghost(game.image[4][0], game, "blinky")
inky = game.createghost(game.image[4][1], game, 'inky')
pinky = game.createghost(game.image[4][2], game, "pinky")
clyde = game.createghost(game.image[4][3], game, "clyde")
game.tableghost = [blinky, inky, pinky, clyde]
game.pacman = Pacman(game)
game.create()

root.mainloop()
