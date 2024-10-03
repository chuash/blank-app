import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://www.google.com",
        "About": "https://www.cccs.gov.sg/",
    },
)

st.title("Uber pickups in NYC")
st.text_input("Your name, please", key="nameholder")
st.write(f"Hello, {st.session_state.nameholder} \n")

add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
