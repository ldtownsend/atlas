import streamlit as st


def display_board(game):
    board = game.board

    for territory in board.territories:
        # Display each territory as a tile
        tile = st.container(height=150)
        with tile:
            tile_name, tile_owner = st.columns([2, 1])

            with tile_name:
                st.markdown(f"#### {territory.name}")

            with tile_owner:
                owner = territory.owner.name if territory.owner else "Unclaimed"
                st.markdown(f"Owner: {owner}")

                # Round 0 - Claim Phase
                if game.round_number == 0:
                    if territory.owner is None:
                        if st.button(label="Claim", key=f"Claim-{territory.name}"):

                            # Update territory ownership directly
                            current_player = game.turn_manager.get_current_player()
                            territory.owner = current_player

                            # Move to the next player's turn
                            game.turn_manager.next_player()

                            # Refresh the UI
                            st.rerun()


def game_status(game):
    current_player = game.turn_manager.get_current_player()
    st.markdown(
        f"""
        **Round:** {game.round_number}\n
        **Current Player:** {current_player}
        """
    )
    st.divider()


def player_stats(players):
    for player in players:
        st.write(f"**{player.name}**")
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
        display_board(game=game)

    # Right column: Print all attributes of the game object
    with right_col:
        st.write("### Game Object Attributes")

        st.write("### Territories")
        for territory in game.board.territories:
            st.write(f"**Territory Name:** {territory.name}")
            st.write(f"**Neighbors:** {territory.neighbors}")
            st.write(f"**Owner:** {territory.owner.name if territory.owner else 'Unclaimed'}")
            st.divider()