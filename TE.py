import math
import plotly.figure_factory as ff
import numpy as np

PI = math.pi




def handleTE(st,modes=[0,0],type_of_waveguide="Rectangular",A=10,B=5,R=5):
    if type_of_waveguide == "Rectangular":
        x = np.linspace(-1, A, 100)
        y = np.linspace(-1, B, 100)
        X,Y = np.meshgrid(x, y)
        M = int(modes[0])
        N = int(modes[1])
        u = np.cos(M*PI/A*X)*np.sin(N*PI/B*Y)
        v = np.sin(M*PI/A*X)*np.cos(N*PI/B*Y)
        
        fig = ff.create_streamline(x, y, u, v, arrow_scale=.1)
        st.plotly_chart(fig)
        # N = 50
        # x_start, x_end = -2.0, 2.0
        # y_start, y_end = -1.0, 1.0
        # x = np.linspace(x_start, x_end, N)
        # y = np.linspace(y_start, y_end, N)
        # X, Y = np.meshgrid(x, y)
        # source_strength = 5.0
        # x_source, y_source = -1.0, 0.0


        # u = (source_strength/(2*np.pi) * (X - x_source)/((X - x_source)**2 + (Y - y_source)**2))
        # v = (source_strength/(2*np.pi) * (Y - y_source)/((X - x_source)**2 + (Y - y_source)**2))

        # st.write(u)
        # fig = ff.create_streamline(x, y, u, v, name='streamline') 
        # st.plotly_chart(fig)   
        

    else:
        pass