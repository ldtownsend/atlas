from game.game import Game


def main():
    game = Game()

    game.initialize_game()

    for player in game.players:
        player.describe()

    game.board.describe()


if __name__ == "__main__":
    main()
