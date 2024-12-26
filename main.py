from game.game import Game
from ui import ui_handler

import streamlit as st


def main():
    if "game" not in st.session_state:
        st.session_state.game = Game()

    st.session_state.game.initialize_game()

    ui_handler.layout(st.session_state.game)


if __name__ == "__main__":
    main()
