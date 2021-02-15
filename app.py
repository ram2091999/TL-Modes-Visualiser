import numpy as np
import os
import pickle
import streamlit as st
import sys
import pandas as pd
from TE import handleTE
from TM import handleTM
from TEM import handleTEM
from QTEM import handle_QTEM

A = 10
B = 5
R = 5


def main():

    st.set_page_config(page_title="Waveguide Visualiser", page_icon=None)

    st.title("Waveguide Modes Visualiser")
    st.subheader("An application to visualise E and H fields inside a waveguide for different modes")

    st.sidebar.title('Choose your preferences below')

    type_of_wave = st.sidebar.radio("Select Mode",['TE','TM','TEM', 'Quasi-TEM (In Progress)'])

    if type_of_wave == "TEM":
        handleTEM(st)
        return

    elif type_of_wave == "Quasi-TEM (In Progress)":
        handle_QTEM(st)
        return

    all_modes = ['m','n','p']
    
    st.sidebar.write("Select shape of waveguide")

    if st.sidebar.checkbox('Rectangular waveguide'):

        modes = all_modes[:2]

        for i, mode in enumerate(modes):
            modes[i] = st.sidebar.slider(mode, 0, 10, 0, 1)
            
        if type_of_wave == "TE":
            handleTE(st,modes,"Rectangular",A=A,B=B)
        elif type_of_wave == "TM":
            handleTM(st,modes,"Rectangular",A=A,B=B)
        else:
            handleTEM(st)
            return
          


    elif st.sidebar.checkbox('Cylindrical waveguide'):

        modes = all_modes[1:]
        
        for i, mode in enumerate(modes):
            modes[i] = st.sidebar.slider(mode, 0, 10, 0, 1)

        if type_of_wave == "TE":
            handleTE(st,modes,"Cylindrical",R = R)
        elif type_of_wave == "TM":
            handleTM(st,modes,"Cylindrical",R = R)
        else:
            handleTEM(st)
            return
    

    st.sidebar.title('About the application')
    st.sidebar.write(
        """This is an interactive web application on pictorial
         representation on EM modes in rectangular and circular waveguides
        """
    )
    st.sidebar.write(
        """You can choose the type of waveguide, and then select the values of modes 
            as required 
        """
    )
    st.sidebar.write(
        """After this, you can visualise the fields in an interactive manner, on the right!
        """
    )

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


if __name__ == "__main__":
    main()
