from game.game import Game
import streamlit as st


def ui_board(board):

    for territory in board.territories:
        tile = st.container(height=100)
        with tile:
            tile_name, tile_owner = st.columns([2, 1])
            with tile_name:
                st.markdown(f"#### {territory.name}")

            with tile_owner:
                st.markdown(f"Owner: {territory.owner}")

            st.markdown(f"Neighbors: {territory.neighbors}")


def ui_player_stats(players):
    for player in players:
        st.write(player.name)
        st.write(f"Available Units: {player.available_units}")
        st.write(f"Coin Balance: {player.coin_balance}")
        st.divider()


def ui_layout(game):
    left_col, middle_col, right_col = st.columns([1, 2, 1])
    with left_col:
        ui_player_stats(players=game.players)

    with middle_col:
        ui_board(board=game.board)

    with right_col:
        st.write("Game Controls To Go Here?")


def main():
    game = Game()

    game.initialize_game()

    for player in game.players:
        player.describe()

    game.board.describe()

    ui_layout(game)


if __name__ == "__main__":
    main()
