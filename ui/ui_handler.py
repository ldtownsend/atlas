import streamlit as st
import random


def per_round_distribution():
    for territory_name in st.session_state["Territories"]:

        territory = st.session_state[f"Territory-{territory_name}"]
        territory["units"] += territory["units_per_round"]


def end_round():
    st.session_state.round_number += 1
    st.session_state.current_player = st.session_state.Players[0]
    per_round_distribution()
    st.rerun()


def _next_player(players, current_player):
    current_index = players.index(current_player)
    next_index = (current_index - 1) % len(players)
    return players[next_index]


def end_turn():
    if (
        st.session_state.round_number > 0
        and st.session_state.current_player == st.session_state.Players[-1]
    ):
        end_round()

    else:
        next_player = _next_player(
            players=st.session_state["Players"],
            current_player=st.session_state.current_player,
        )
        st.session_state.current_player = next_player


def initialize_unit_distribution(territory):
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
                end_turn()
                st.rerun()  # Refresh UI after deployment


def determine_winner(defending_units, attacking_units):
    if defending_units > attacking_units:
        return "defender", defending_units
    else:
        return "attacker", attacking_units


def combat(defending_units, attacking_units):
    while min(defending_units, attacking_units) > 0:
        defender_roll = random.randint(0, 9)
        attacker_roll = random.randint(0, 9)

        if defender_roll > attacker_roll:
            attacking_units -= 1
        elif defender_roll < attacker_roll:
            defending_units -= 1
        else:
            pass

        # print(f"Attacker Roll: {attacker_roll}; Defender Roll: {defender_roll}")
        # print(f"Attacker Units: {attacking_units}; Defender Units: {defending_units}")

    return defending_units, attacking_units


def move_units(units, origin, destination):
    origin_territory = st.session_state[f"Territory-{origin}"]
    destination_territory = st.session_state[f"Territory-{destination}"]

    origin_territory["units"] -= units

    if destination_territory["owner"] == st.session_state.current_player:
        destination_territory["units"] += units

        target_unit_count = origin_territory["units"]
        st.write(f"Moving {target_unit_count} to ... {destination}")
        st.rerun()

    else:
        # Call function with combat logic here

        defending_units, attacking_units = combat(
            defending_units=destination_territory["units"], attacking_units=units
        )
        winner, remaining_units = determine_winner(defending_units, attacking_units)

        if winner == "attacker":
            destination_territory["owner"] = origin_territory["owner"]
        destination_territory["units"] = remaining_units

        end_turn()
        st.rerun()


def unit_activity(territory):
    with st.form(key=f"territory_options_form_{territory['name']}"):
        neighbors = territory["neighbors"]
        max_units = territory["units"]

        unit_count_col, destination_col = st.columns(2)

        with unit_count_col:
            unit_count = st.number_input(
                "Move Units",
                value=0,
                step=1,
                max_value=max_units,
                min_value=0,
                placeholder="Number of Units to Move",
            )

        with destination_col:
            units_destination = st.pills("Neighboring Territories", options=neighbors)

        button_col, message_col = st.columns(2)

        with button_col:
            territory_action_button = st.form_submit_button("Move Units")

        with message_col:
            if territory_action_button:
                move_units(
                    units=unit_count,
                    origin=territory["name"],
                    destination=units_destination,
                )


def territory_actions(territory):
    if territory["owner"] == st.session_state.current_player:
        unit_activity(territory)


def main_loop():
    pass


def display_board():
    for territory_name in st.session_state["Territories"]:
        # Retrieve territory data
        territory = st.session_state[f"Territory-{territory_name}"]

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
                        initialize_unit_distribution(territory=territory)

                else:
                    territory_actions(territory=territory)
                    # add the next steps for how do get more units from each territory
                    # add how to attack/pass at the end of a turn
                    # create combat module
                    pass


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
    with st.sidebar:
        # with st.container(height=650):
        #     st.write(st.session_state)
        game_status(game)
        player_stats(players=game.players)
        if st.button(label="End Turn"):
            end_turn()
            st.rerun()

    display_board()

    # Right column: Print all attributes of the game object
    # with right_col:
    #     st.write("### Game Object Attributes")

    st.write(st.session_state.Players[-1])

    st.write(st.session_state)
    # st.write("### Territories")
    # for territory in game.board.territories:
    #     st.write(f"**Territory Name:** {territory.name}")
    #     st.write(f"**Neighbors:** {territory.neighbors}")
    #     st.write(f"**Owner:** {territory.owner.name if territory.owner else 'Unclaimed'}")
    #     st.divider()
