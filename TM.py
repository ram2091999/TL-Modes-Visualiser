import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import special
from functions_rect import TE_TM_Functions
from functions_circular import Circular_TE_TM_Functions


PI = math.pi




def handleTM(st,modes=[0,0],type_of_waveguide="Rectangular",A=10,B=5,R=5):
    if type_of_waveguide == "Rectangular":
        x = np.linspace(0, A, 101)
        y = np.linspace(0, B, 101)
        X,Y = np.meshgrid(x, y)
        M = int(modes[0])
        N = int(modes[1])
        par = TE_TM_Functions(M,N,A,B)
        if M==0 and N==0:
            st.error("m and n cannot be 0 at the same time")
            return
        u = np.cos(M*PI/A*X)*np.sin(N*PI/B*Y)
        v = np.sin(M*PI/A*X)*np.cos(N*PI/B*Y)
        fig, ax = plt.subplots()
        plt.streamplot(x,y,u,v,color="xkcd:azure")
        col1, col2 = st.beta_columns(2)
        col1.header("E Field")
        col2.header("H Field")
        plt.axis("scaled")
        col1.pyplot(fig)
        u = np.sin(M*PI/A*X)*np.cos(N*PI/B*Y)
        v = np.cos(M*PI/A*X)*np.sin(N*PI/B*Y)
        fig, ax = plt.subplots()
        plt.streamplot(x,y,u,v,color="xkcd:azure")
        plt.axis("scaled")
        col2.pyplot(fig)
        st.write(pd.DataFrame({
           'Parameter': ["Kc", "Fc", "Beta-g", "Vg","Zin","Zg","lambda-g"],
           'Value': [par.Kc(),par.Fc(), par.beta_g(),par.v_G(),par.Z_in(),par.Z_G_TM(),par.lambda_G()]
       }))
          

    else:
        r = np.linspace(0,R,101)
        t = np.linspace(0,2*PI,101)
        T,RAD = np.meshgrid(t,r)
        N = int(modes[0])
        P = int(modes[1])
        if P == 0:
            st.error("p cannot be 0!")
            return
        X = special.jn_zeros(N,P)
        U = special.jvp(N,X[-1].round(3)/R*RAD)*np.cos(N*T)
        V = special.jv(N,X[-1].round(3)/R*RAD)*np.sin(N*T)
        col1, col2 = st.beta_columns(2)
        col1.header("E Field")
        col2.header("H Field")
        par = Circular_TE_TM_Functions(N,P,R)
        fig,ax = plt.subplots()
        plt.polar(2*PI,R)
        plt.streamplot(T,RAD,V,U)
        plt.axis("scaled")

        col1.pyplot(fig)
        U = special.jv(N,X[-1].round(3)/R*RAD)*np.sin(N*T)
        V = special.jvp(N,X[-1].round(3)/R*RAD)*np.cos(N*T)

        fig,ax = plt.subplots()
        plt.polar(2*PI,R)
        plt.streamplot(T,RAD,V,U)
        plt.axis("scaled")
        col2.pyplot(fig)
        st.write(pd.DataFrame({
           'Parameter': ["Kc", "Fc", "Beta-g", "Vg","Zin","Zg","lambda-g"],
           'Value': [par.Kc_TM(),par.Fc_TM(), par.beta_g_TM(),par.v_G_TM(),par.Z_in(),par.Z_G_TM(),par.lambda_G_TM()]
       }))
