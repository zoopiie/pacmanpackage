import keyboard


def bind_controls(game):
    keyboard.on_press_key("space", lambda _: game.changelevel())
    keyboard.on_press_key("enter", lambda _: game.inviciblemode())
    keyboard.on_press_key("up", lambda _: game.pacman.move('up'))
    keyboard.on_press_key("left", lambda _: game.pacman.move('left'))
    keyboard.on_press_key("down", lambda _: game.pacman.move('down'))
    keyboard.on_press_key("right", lambda _: game.pacman.move('right'))
    keyboard.on_press_key("0", lambda _: game.ghostbreaker())
    keyboard.on_press_key("tab", lambda _: game.morelife())
    keyboard.on_press_key("ctrl", lambda _: game.defeatevent())
    keyboard.on_press_key("F1", lambda _: game.tricheplus())
    keyboard.on_press_key("F3", lambda _: game.pointadd())
    keyboard.on_press_key("F2", lambda _: game.discret())
