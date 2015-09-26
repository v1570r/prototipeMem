
import sys

from game import Game



def run():
    g = Game(480, 480)

    g.init()

    while g.running:
        g.eventHandle()
        g.render()

    g.quit()
    return 0


if __name__ == "__main__":
    sys.exit(run())
