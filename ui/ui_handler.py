import streamlit as st


def _next_player(players, current_player):
    current_index = players.index(current_player)
    next_index = (current_index - 1) % len(players)
    return players[next_index]


def end_turn():
    next_player = _next_player(
        players=st.session_state["Players"],
        current_player=st.session_state.current_player,
    )
    st.session_state.current_player = next_player


def end_round():
    st.session_state.round_number += 1
    st.session_state.current_player = st.session_state.Players[0]


def initialize_unit_distribution(st_territory, territory):
    if territory["owner"] is None:
        with st.form(key=f"claim_form_{territory['name']}"):
            claim_button = st.form_submit_button("Claim Territory")

            if claim_button:
                # Assign ownership and deploy 1 unit
                territory["owner"] = st.session_state.current_player
                territory["units"] += 1

                st.session_state[st.session_state.current_player][
                    "available_units"
                ] -= 1

                st.session_state[f"Territory-{st_territory}"] = territory
                end_turn()
                st.rerun()  # Refresh UI after claim

    # DEPLOY UNITS FORM
    if territory["owner"] == st.session_state.current_player:
        with st.form(key=f"deploy_form_{territory['name']}"):
            deploy_units = st.number_input(
                "Deploy Units",
                value=0,
                step=1,
                max_value=st.session_state[st.session_state.current_player][
                    "available_units"
                ],
                placeholder="Number of Units",
            )

            st.session_state[st.session_state.current_player][
                "available_units"
            ] -= deploy_units

            deploy_button = st.form_submit_button("Deploy Units")

            if deploy_button and deploy_units > 0:
                # Deploy additional units
                territory["units"] += deploy_units
                st.session_state[f"Territory-{st_territory}"] = territory
                end_turn()
                st.rerun()  # Refresh UI after deployment


def display_board():
    for st_territory in st.session_state["Territories"]:
        # Retrieve territory data
        territory = st.session_state[f"Territory-{st_territory}"]

        # Create a tile for each territory
        tile = st.container(height=200)

        with tile:
            # Create columns for layout
            tile_name, tile_action = st.columns([1, 1])

            # Display Territory Name and Units
            with tile_name:
                st.markdown(f"#### {territory['name']}")
                st.write(f"Units: {territory['units']}")
                owner = territory["owner"] if territory["owner"] else "Unclaimed"
                st.markdown(f"Owner: {owner}")

            with tile_action:

                if st.session_state.round_number == 0:
                    total_available_units = 0
                    for player in st.session_state.Players:
                        total_available_units += st.session_state[player][
                            "available_units"
                        ]
                        pass
                    if total_available_units == 0:
                        end_round()

                    else:
                        initialize_unit_distribution(
                            st_territory=st_territory, territory=territory
                        )


def game_status(game):
    current_player = st.session_state.current_player
    st.markdown(
        f"""
        **Round:** {st.session_state.round_number}\n
        **Current Player:** {current_player}
        """
    )
    st.divider()


def player_stats(players):
    for player_str in st.session_state.Players:
        player = st.session_state[player_str]
        st.write(f"**{player['name']}**")
        st.write("Available Units: ", player["available_units"])
        st.write("Coin Balance: ", player["coin_balance"])
        st.divider()


def layout(game):
    st.set_page_config(layout="wide")

    # Primary Game Canvas
    left_col, middle_col = st.columns([1, 3])
    with left_col:
        # with st.container(height=650):
        #     st.write(st.session_state)
        game_status(game)
        player_stats(players=game.players)
        if st.button(label="End Turn"):
            end_turn()
            st.rerun()

    with middle_col:
        display_board()

    # Right column: Print all attributes of the game object
    # with right_col:
    #     st.write("### Game Object Attributes")

    st.write(st.session_state)
    # st.write("### Territories")
    # for territory in game.board.territories:
    #     st.write(f"**Territory Name:** {territory.name}")
    #     st.write(f"**Neighbors:** {territory.neighbors}")
    #     st.write(f"**Owner:** {territory.owner.name if territory.owner else 'Unclaimed'}")
    #     st.divider()
