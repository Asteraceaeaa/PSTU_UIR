import numpy as np
import scipy.integrate as integrate
import sympy.integrals as integrals
import matplotlib.pyplot as plt

def maltus_model(t, x0, alpha):
    return x0*np.exp(alpha*t)

t = np.linspace(0, 50, 100)
a = 0.1
b = 0.1

x = maltus_model(t, b, a)

plt.figure(figsize=(10, 6))
plt.plot(t, x, linewidth=2)
plt.xlabel('Время t', fontsize=16)
plt.ylabel('Численность x', fontsize=16)
plt.title('Численность популяции. Модель Мальтуса', fontsize=16)
plt.grid(True, alpha=0.3)
plt.show()