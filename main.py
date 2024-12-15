from game.game import Game
from ui import ui_handler


def main():
    game = Game()

    game.initialize_game()

    ui_handler.layout(game)


if __name__ == "__main__":
    main()
