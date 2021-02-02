import streamlit as st
import numpy as np 
import pandas as pd 


st.set_page_config(page_title="WG Visualiser", page_icon=None)


# CONSTANTS

MODE_OF_OPERATION = {
    "TE":0,
    "TM":1,
    "TEM":2
}

TYPE_OF_WAVEGUIDE = {
    "Rectangular":0,
    "Circular":1
}



#SIDE BAR HANDLER


mode = st.sidebar.selectbox(
    "Select your mode",
    [
        "TE",
        "TM",
        "TEM"
    ]
)

type_of_waveguide = st.sidebar.selectbox(
    "Select Type of waveguide",
    [
        "Rectangular",
        "Circular"
    ]
)

m = st.sidebar.slider(
    "m:",
    0,
    10,
    0,
    1
)

n = st.sidebar.slider(
    "n:",
    0,
    10,
    0,
    1
)



#MAIN APP


st.title("Waveguide Modes Visualiser")
st.subheader("An application to visualise E and H fields inside a waveguide for different modes")

st.write(mode)
st.write(type_of_waveguide)