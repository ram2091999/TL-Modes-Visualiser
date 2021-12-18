import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.constants import *
from scipy import special


PI = math.pi


class Circular_TE_TM_Functions:
    def __init__(self, n, p, a):
        self.n = n
        self.p = p
        self.a = a
        self.X_np = special.jn_zeros(n, p)[-1]
        self.dX_np = special.jnp_zeros(n, p)[-1]
        self.f_TE = 2 * self.Fc_TE()
        self.f_TM = 2 * self.Fc_TM()
        self.w_TE = 2 * PI * self.f_TE
        self.w_TM = 2 * PI * self.f_TM

    def Kc_TE(self):
        val = self.dX_np / self.a
        return val

    def Fc_TE(self):
        val = (1 / (2 * PI * self.a * np.sqrt(mu_0 * epsilon_0))) * self.dX_np
        return val

    def beta_g_TE(self):
        term1 = (self.w_TE ** 2) * mu_0 * epsilon_0
        term2 = np.power((self.dX_np / self.a), 2)
        val = np.sqrt(term1 - term2)
        return val

    def v_G_TE(self):
        beta_G_val = self.beta_g_TE()
        val = self.w_TE / beta_G_val
        return val

    def Z_in(self):
        val = np.sqrt(mu_0 / epsilon_0)
        return val

    def Z_G_TE(self):
        fc_val = self.Fc_TE()
        Z_in = self.Z_in()
        val = Z_in / (np.sqrt(1 - np.power((fc_val / self.f_TE), 2)))
        return val

    def lambda_G_TE(self):
        beta_G_val = self.beta_g_TE()
        val = 2 * PI / beta_G_val
        return val

    def Kc_TM(self):
        val = self.X_np / self.a
        return val

    def beta_g_TM(self):
        term1 = (self.w_TM ** 2) * mu_0 * epsilon_0
        term2 = np.power((self.X_np / self.a), 2)
        val = np.sqrt(term1 - term2)
        return val

    def Fc_TM(self):
        val = (1 / (2 * PI * self.a * np.sqrt(mu_0 * epsilon_0))) * self.X_np
        return val

    def lambda_G_TM(self):
        beta_G_val = self.beta_g_TM()
        val = 2 * PI / beta_G_val
        return val

    def Z_G_TM(self):
        fc_val = self.Fc_TM()
        Z_in = self.Z_in()
        val = Z_in * (np.sqrt(1 - np.power((fc_val / self.f_TM), 2)))
        return val

    def v_G_TM(self):
        beta_G_val = self.beta_g_TM()
        val = self.w_TM / beta_G_val
        return val
