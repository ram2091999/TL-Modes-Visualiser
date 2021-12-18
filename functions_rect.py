import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.constants import *

PI = math.pi


class TE_TM_Functions:
    def __init__(self, m, n, a, b):
        self.m = m
        self.n = n
        self.a = a
        self.b = b
        self.f = 2 * self.Fc()
        self.w = 2 * PI * self.f

    def Kc(self):
        val = np.power((self.m * PI / self.a), 2) + np.power((self.n * PI / self.b), 2)
        return np.sqrt(val)

    def Fc(self):
        val = (1 / (2 * np.sqrt(mu_0 * epsilon_0))) * np.sqrt(
            np.power((self.m / self.a), 2) + np.power((self.n / self.b), 2)
        )
        return val

    def beta_g(self):
        fc_val = self.Fc()
        val = (
            self.w
            * np.sqrt(mu_0 * epsilon_0)
            * np.sqrt(1 - np.power((fc_val / self.f), 2))
        )
        return val

    def v_G(self):
        beta_G_val = self.beta_g()
        val = self.w / beta_G_val
        return val

    def Z_in(self):
        val = np.sqrt(mu_0 / epsilon_0)
        return val

    def Z_G_TE(self):
        fc_val = self.Fc()
        Z_in = self.Z_in()
        val = Z_in / (np.sqrt(1 - np.power((fc_val / self.f), 2)))
        return val

    def lambda_G(self):
        beta_G_val = self.beta_g()
        val = 2 * PI / beta_G_val
        return val

    def Z_G_TM(self):
        fc_val = self.Fc()
        Z_in = self.Z_in()
        val = Z_in * (np.sqrt(1 - np.power((fc_val / self.f), 2)))
        return val


class TEM_Functions:
    def __init__(self):
        self.w = 18836000.01

    def Kc(self):
        val = 0
        return val

    def Fc(self):
        val = 0
        return val

    def Z_in(self):
        val = np.sqrt(mu_0 / epsilon_0)
        return val

    def beta_g(self):
        val = self.w * np.sqrt(mu_0 * epsilon_0)
        return val

    def v_G(self):
        beta_g_val = self.beta_g()
        val = self.w / beta_g_val
        return val


# if __name__ == '__main__':
#     m = 1
#     n = 1
#     a = 10
#     b = 5
#     tester = TEM_Functions()
#     kc = tester.Z_in()
#     print(kc)
