from tkinter import *

class Floor(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.file = PhotoImage(file="floor.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)

class Wall(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.file = PhotoImage(file="wall.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)

class Hero(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.file = PhotoImage(file="hero_down.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)
    def MoveUp(self):
        canvas.delete(self.img)
        self.file = PhotoImage(file="hero_up.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)
    def MoveDown(self):
        canvas.delete(self.img)
        self.file = PhotoImage(file="hero_down.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)
    def MoveRight(self):
        canvas.delete(self.img)
        self.file = PhotoImage(file="hero_right.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)
    def MoveLeft(self):
        canvas.delete(self.img)
        self.file = PhotoImage(file="hero_left.gif")
        self.img = canvas.create_image(self.X, self.Y, image=self.file, anchor=NW)

root = Tk()

canvas = Canvas(root, width=720, height=720)

canvas.pack()

canvas.focus_set()

floor = []
board = [[0, 0, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]]
for row, i in enumerate(board, start=0):
    for column, j in enumerate(i, start=0):
        if j == 0:
            floor.append(Floor(column*72, row*72))
        elif j == 1:
            floor.append(Wall(column*72, row*72))

hero = Hero(0, 0)
def is_floor(X, Y):
    return board[int(Y/72)][int(X/72)] == 0


def on_key_press(e):
    if e.keycode == 38:
        if hero.Y - 72 >= 0:
            if is_floor(hero.X, hero.Y-72):
                hero.Y = hero.Y-72
        hero.MoveUp()
    elif e.keycode == 40:
        if hero.Y + 72 <= 648:
            if is_floor(hero.X, hero.Y+72):
                hero.Y = hero.Y+72
        hero.MoveDown()
    elif e.keycode == 37:
        if hero.X - 72 >= 0:
            if is_floor(hero.X-72, hero.Y):
                hero.X = hero.X-72
        hero.MoveLeft()
    elif e.keycode == 39:
        if hero.X + 72 <= 648:
            if is_floor(hero.X + 72, hero.Y):
                hero.X = hero.X+72
        hero.MoveRight()


canvas.bind("<KeyPress>", on_key_press)

root.mainloop()