import numpy as np
import os
import pickle
import streamlit as st
import sys
import pandas as pd


def main():

    st.set_page_config(page_title="Waveguide Visualiser", page_icon=None)

    st.title("Waveguide Modes Visualiser")
    st.subheader("An application to visualise E and H fields inside a waveguide for different modes")
    
    st.sidebar.title('Choose your preferences below')

    all_modes = ['m','n','p']

    if st.sidebar.checkbox('Rectangular waveguide'):

        modes = all_modes[:2]

        for mode in modes:
            modes[mode] = st.sidebar.slider(mode, 0, 10, 0, 1)

    elif st.sidebar.checkbox('Cylindrical waveguide'):

        modes = all_modes[1:]
        
        for mode in modes:
            modes[mode] = st.sidebar.slider(mode, 0, 10, 0, 1)


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


if __name__ == "__main__":
    main()