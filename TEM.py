import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import special


PI = math.pi
A = 4
B = 8


def handleTEM(st):
    r = np.linspace(A,B,101)
    t = np.linspace(0,2*PI,101)
    T,RAD = np.meshgrid(t,r)
    U = 10/RAD
    V = T*0
    col1, col2 = st.beta_columns(2)
    col1.header("E Field")
    col2.header("H Field")
    fig,ax = plt.subplots()
    plt.polar(2*PI,B)
    plt.streamplot(T,RAD,V,U)
    plt.axis("scaled")
    col1.pyplot(fig)
    U = 0.000000001*RAD
    V=T*100
    fig,ax = plt.subplots()
    plt.polar(2*PI,B)
    plt.streamplot(T,RAD,V,U,density=1)
    plt.axis("scaled")
    col2.pyplot(fig)

