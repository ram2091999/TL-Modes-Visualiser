import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy.constants import *

PI = math.pi

# Functions to be included -
# Rectangular
# 1. Kc
# 2. Fc
# 3. Beta_G
# 4. v_G
# 5. Z_G
# 6. Z_in
# 7. Lambda_G

# Circular - Either include in the same func with an if stmt or make a new class --- TODO
# 1. Beta_G
# 2. Z_G
# 3. Fc
# 4. Kc
# 5. v_G
# 6. Lambda_G
# 7. Xnp table


class TE_TM_Functions:
    def Kc(self, m, n, a, b):
        val = np.power((m * PI / a), 2) + np.power((n * PI / b), 2)
        return np.sqrt(val)

    def Fc(self, m, n, a, b):
        val = (1 / np.sqrt(mu_0 * epsilon_0)) * np.power((m / a), 2) + np.power(
            (n / b), 2
        )
        return val

    def beta_g(self, w, f, m, n, a, b):
        fc_val = self.Fc(m, n, a, b)
        val = w * np.sqrt(mu_0 * epsilon_0) * np.sqrt(1 - np.power((fc_val / f), 2))
        return val

    def v_G(self, w, f, m, n, a, b):
        beta_G_val = self.beta_g(w, f, m, n, a, b)
        val = w / beta_G_val
        return val

    def Z_in(self):
        val = np.sqrt(mu_0 / epsilon_0)
        return val

    def Z_G_TE(self, f, m, n, a, b):
        fc_val = self.Fc(m, n, a, b)
        Z_in = self.Z_in()
        val = Z_in / (np.sqrt(1 - np.power((fc_val / f), 2)))
        return val

    def lambda_G(self, w, f, m, n, a, b):
        beta_G_val = self.beta_g(w, f, m, n, a, b)
        val = 2 * PI / beta_G_val
        return val

    def Z_G_TM(self, f, m, n, a, b):
        fc_val = self.Fc(m, n, a, b)
        Z_in = self.Z_in()
        val = Z_in * (np.sqrt(1 - np.power((fc_val / f), 2)))
        return val


class TEM_Functions:
    def Kc(self):
        val = 0
        return val

    def Fc(self):
        val = 0
        return val

    def Z_in(self):
        val = np.sqrt(mu_0 / epsilon_0)
        return val

    def beta_g(self, w):
        val = w * np.sqrt(mu_0 * epsilon_0)
        return val

    def v_G(self, w):
        beta_g_val = self.beta_g(w)
        val = w / beta_g_val
        return val
