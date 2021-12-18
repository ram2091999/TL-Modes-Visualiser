import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from functions_rect import TEM_Functions
import pandas as pd

PI = math.pi
A = 4
B = 8


def handleTEM(st):
    r = np.linspace(A, B, 101)
    t = np.linspace(0, 2 * PI, 101)
    T, RAD = np.meshgrid(t, r)
    U = 10 / RAD
    V = T * 0
    par = TEM_Functions()
    fig, ax = plt.subplots()
    plt.polar(2 * PI, B)
    plt.streamplot(T, RAD, V, U, color="xkcd:azure")
    plt.axis("scaled")
    st.subheader("E field")
    st.pyplot(fig)
    U = 0.000000001 * RAD
    V = T * 100
    fig, ax = plt.subplots()
    plt.polar(2 * PI, B)
    plt.streamplot(T, RAD, V, U, color="red")
    plt.axis("scaled")
    st.subheader("H field")
    st.pyplot(fig)
    st.subheader("Values")
    st.write(
        pd.DataFrame(
            {
                "Parameter": ["Kc", "Fc", "Beta-g", "Vg"],
                "Value": [par.Kc(), par.Fc(), par.beta_g(), par.v_G()],
                "Unit": ["1/m", "Hz", "1/m", "m/s"],
            }
        )
    )
