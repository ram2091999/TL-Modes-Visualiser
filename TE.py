import math
import matplotlib.pyplot as plt
import numpy as np

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
        pass