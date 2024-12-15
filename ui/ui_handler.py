import streamlit as st


def display_board(board):
    for territory in board.territories:
        tile = st.container(height=100)
        with tile:
            tile_name, tile_owner = st.columns([2, 1])
            with tile_name:
                st.markdown(f"#### {territory.name}")

            with tile_owner:
                st.markdown(f"Owner: {territory.owner}")

            st.markdown(f"Neighbors: {territory.neighbors}")


def game_status(game):
    current_player = game.turn_manager.get_current_player()
    st.markdown(
        f"""
        Round: {game.round_number}\n
        Current Player: {current_player}
        """
    )

    st.divider()


def player_stats(players):
    for player in players:
        st.write(player.name)
        st.write(f"Available Units: {player.available_units}")
        st.write(f"Coin Balance: {player.coin_balance}")
        st.divider()


def layout(game):
    st.set_page_config(layout="wide")

    left_col, middle_col, right_col = st.columns([1, 2, 1])
    with left_col:
        game_status(game)
        player_stats(players=game.players)

    with middle_col:
        display_board(board=game.board)

    with right_col:
        st.write("Game Controls To Go Here?")
