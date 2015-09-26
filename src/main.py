
import sys

from game import Game



def run():
    g = Game(800, 600)

    g.init()

    while g.running:
        g.eventHandle()
        g.render()
        g.update()

    g.quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())
