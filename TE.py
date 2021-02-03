import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import special


PI = math.pi




def handleTE(st,modes=[0,0],type_of_waveguide="Rectangular",A=10,B=5,R=5):
    if type_of_waveguide == "Rectangular":
        x = np.linspace(0, A, 101)
        y = np.linspace(0, B, 101)
        X,Y = np.meshgrid(x, y)
        M = int(modes[0])
        N = int(modes[1])
        u = np.cos(M*PI/A*X)*np.sin(N*PI/B*Y)
        v = np.sin(M*PI/A*X)*np.cos(N*PI/B*Y)
        fig, ax = plt.subplots()
        plt.streamplot(x,y,u,v,color="xkcd:azure")
        plt.axis("scaled")
        st.write("E field")
        st.pyplot(fig)
        u = np.sin(M*PI/A*X)*np.cos(N*PI/B*Y)
        v = np.cos(M*PI/A*X)*np.sin(N*PI/B*Y)
        fig, ax = plt.subplots()
        plt.streamplot(x,y,u,v,color="xkcd:azure")
        plt.axis("scaled")
        st.write("H field")
        st.pyplot(fig)
          

    else:
        r = np.linspace(0,R,101)
        t = np.linspace(0,2*PI,101)
        T,RAD = np.meshgrid(t,r)
        N = int(modes[0])
        P = int(modes[1])
        X = special.jnp_zeros(N,P)
        U = special.jv(N,X[-1].round(3)/R*RAD)*np.sin(N*T)
        V = special.jvp(N,X[-1].round(3)/R*RAD)*np.cos(N*T)
        fig,ax = plt.subplots()
        plt.polar(2*PI,R)
        plt.streamplot(T,RAD,V,U)
        plt.axis("scaled")
        st.pyplot(fig)
        U = -1*special.jv(N,X[-1].round(3)/R*RAD)*np.cos(N*T)
        V = special.jv(N,X[-1].round(3)/R*RAD)*np.sin(N*T)
        fig,ax = plt.subplots()
        plt.polar(2*PI,R)
        plt.streamplot(T,RAD,V,U)
        plt.axis("scaled")
        st.pyplot(fig)
