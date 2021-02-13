import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from functions_rect import TEM_Functions
import pandas as pd
from matplotlib.patches import Rectangle

PI = math.pi
A = 4
B = 8

def cuboid_data(center, size):

    # suppose axis direction: x: to left; y: to inside; z: to above
    # get the (left, outside, bottom) point
    o = [a- b/ 2 for a, b in zip(center, size)]
    # get the length, width, and height
    l, w, h = size
    x = [[o[0], o[0] + l, o[0] + l, o[0], o[0]],  # x coordinate of points in bottom surface
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],  # x coordinate of points in upper surface
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],  # x coordinate of points in outside surface
         [o[0], o[0] + l, o[0] + l, o[0], o[0]]]  # x coordinate of points in inside surface

    y = [[o[1], o[1], o[1] + w, o[1] + w, o[1]],  # y coordinate of points in bottom surface
         [o[1], o[1], o[1] + w, o[1] + w, o[1]],  # y coordinate of points in upper surface
         [o[1], o[1], o[1], o[1], o[1]],          # y coordinate of points in outside surface
         [o[1] + w, o[1] + w, o[1] + w, o[1] + w, o[1] + w]]    # y coordinate of points in inside surface

    z = [[o[2], o[2], o[2], o[2], o[2]],                        # z coordinate of points in bottom surface
         [o[2] + h, o[2] + h, o[2] + h, o[2] + h, o[2] + h],    # z coordinate of points in upper surface
         [o[2], o[2], o[2] + h, o[2] + h, o[2]],                # z coordinate of points in outside surface
         [o[2], o[2], o[2] + h, o[2] + h, o[2]]]                # z coordinate of points in inside surface
   
    return np.array(x), np.array(y), np.array(z)



def test(st):
    center = [0, 0, 0]
    length = 60 * 2
    width = 75 * 2
    height = 15 * 2

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y, Z = cuboid_data(center, (length, width, height))
    ax.plot_surface(X, Y, Z, color='green', rstride=1, cstride=1, alpha=.5)


    center2 = [10, -17, 30] #for the thin strip
    length2 = 10 * 2
    width2 = 75 * 2
    height2 = 2 * 2
    X2, Y2, Z2 = cuboid_data(center2, (length2, width2, height2))
    ax.plot_surface(X2, Y2, Z2, color='gold', rstride=1, cstride=1, alpha=1)

    #Comment if you need coordinate reference and grid -----------
    ax.grid(False)

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    #-------------------------------------------------------------

    ax.set_xlim(-100, 100)
  
    ax.set_ylim(-100, 100)

    ax.set_zlim(-100, 100)
    st.pyplot(fig)

def test_coupled(st):
    center = [0, 0, 0]
    length = 60 * 2
    width = 75 * 2
    height = 15 * 2

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y, Z = cuboid_data(center, (length, width, height))
    ax.plot_surface(X, Y, Z, color='green', rstride=1, cstride=1, alpha=.5)


    center2 = [-10, -27, 40] #for the thin strip - left
    length2 = 10 * 2
    width2 = 75 * 2
    height2 = 2 * 2
    X2, Y2, Z2 = cuboid_data(center2, (length2, width2, height2))
    ax.plot_surface(X2, Y2, Z2, color='gold', rstride=1, cstride=1, alpha=1)

    center3 = [35, -17, 30] #for the thin strip - right
    length3 = 10 * 2
    width3 = 75 * 2
    height3 = 2 * 2
    X3, Y3, Z3 = cuboid_data(center3, (length3, width3, height3))
    ax.plot_surface(X3, Y3, Z3, color='gold', rstride=1, cstride=1, alpha=1)

    #Comment if you need coordinate reference and grid -----------
    ax.grid(False)

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    #-------------------------------------------------------------
    ax.set_xlim(-100, 100)

    ax.set_ylim(-100, 100)

    ax.set_zlim(-100, 100)
    st.pyplot(fig)



def CS_single(st):
    fig, ax = plt.subplots()

    ax.plot([0, 0],[0, 0])

    ax.add_patch(Rectangle((-5, -5), 10, 3, color = 'green'))
    ax.add_patch(Rectangle((-1.25, -1.925), 2.5, 0.5, color = 'gold'))

    # ax.set_xlabel('X')
    ax.set_xlim(-10, 10)
    # ax.set_ylabel('Y')
    ax.set_ylim(-10, 10)

    ax.set_xticks([])
    ax.set_yticks([])

    st.pyplot(plt)  


def CS_coupled(st):
    fig, ax = plt.subplots()

    ax.plot([0, 0],[0, 0])

    ax.add_patch(Rectangle((-5, -5), 10, 3, color = 'green'))
    ax.add_patch(Rectangle((-3.5, -1.95), 2.5, 0.5, color = 'gold'))
    ax.add_patch(Rectangle((1, -1.95), 2.5, 0.5, color = 'gold'))

    # ax.set_xlabel('X')
    ax.set_xlim(-10, 10)
    # ax.set_ylabel('Y')
    ax.set_ylim(-10, 10)

    ax.set_xticks([])
    ax.set_yticks([])

    st.pyplot(fig)



def handle_QTEM(st):
    par = TEM_Functions()
    st.header("Single Microstrip Line")
    st.subheader("Full view")    
    test(st)
    st.subheader("Cross-Sectional view") 
    CS_single(st)
    st.header("Coupled Microstrip Line")
    st.subheader("Full view")  
    test_coupled(st)
    st.subheader("Cross-Sectional view") 
    CS_coupled(st)
    #st.header("Values")
    # st.write(pd.DataFrame({
    #        'Parameter': ["Kc", "Fc", "Beta-g", "Vg"],
    #        'Value': [par.Kc(),par.Fc(), par.beta_g(),par.v_G()],
    #        'Unit':["1/m", "Hz", "1/m", "m/s"]

    #    }))

